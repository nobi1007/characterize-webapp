import os
import cv2
from random import randrange
from azure.core.exceptions import ResourceNotFoundError
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

class CustomFileStorage:

    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        self.file_name = ""
        self.saved_file_uri = ""

    def __str__(self):
        return self.user_id+"\t"+self.file_name+"\t"+self.saved_file_uri

    def __container_exists(self, container_client) -> bool:
        try:
            container_client.get_container_properties()
            return True
        except ResourceNotFoundError:
            return False

    def __blob_exists(self, blob_client) -> bool:
        try:
            blob_client.get_blob_properties()
            return True
        except ResourceNotFoundError:
            return False

    def __get_file_suffix(self, file_type: str) -> str:
        if file_type == "image":
            return ".jpg"
        if file_type == "text":
            return ".txt"
        if file_type == "pdf":
            return ".pdf"

    def store_file(self, file_name, file_data, file_type: str) -> None:        
        file_suffix = self.__get_file_suffix(file_type)        
        self.file_name = file_name + file_suffix

        if file_type == "image":
            cv2.imwrite(self.file_name, file_data)

        if file_type == "text":
            temp_file = open(self.file_name,"w")
            temp_file.write(file_data)
            temp_file.close()
        
        # print("file-data",file_data)

        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        container_name = self.user_id
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container = container_name, blob = self.file_name)
        container_client =  ContainerClient.from_connection_string(connect_str,container_name)

        upload_data = file_data
        original_file_name = self.file_name

        with open(self.file_name,"rb") as data:
            upload_data = data
            # print("upload-data",upload_data)

            if self.__container_exists(container_client):
                while self.__blob_exists(blob_client):
                    self.file_name = file_name+str(randrange(1000,9999,19)) + file_suffix
                    blob_client = blob_service_client.get_blob_client(container = container_name, blob = self.file_name)
                blob_client.upload_blob(upload_data)                
            else:
                container_client = blob_service_client.create_container(container_name)
                blob_client = blob_service_client.get_blob_client(container=container_name, blob= self.file_name)
                blob_client.upload_blob(upload_data)

        self.saved_file_uri = blob_client.url
        container_client.set_container_access_policy(signed_identifiers={},public_access="blob")
        os.remove(original_file_name)