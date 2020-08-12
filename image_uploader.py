import os, uuid

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import ResourceNotFoundError


try:
    print("Azure Blob storage v12 - Python quickstart sample")
    # Quick start code goes here
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_name = "characterizeimagestore"
    # container_name = "abc"

    # container_client = blob_service_client.create_container(container_name)
    
    def container_exists(container_client):
        try:
            container_client.get_container_properties()
            return True
        except ResourceNotFoundError:
            return False

    container_client =  ContainerClient.from_connection_string(connect_str,container_name)
    # print(container_client.get_container_properties())
    # Create a file in local data directory to upload and download
    files_to_upload = os.listdir("data")
    local_path = "./data"



    
    for file_name in files_to_upload:
        upload_file_path = os.path.join(local_path, file_name)
        # print(file_name)

        blob_client = blob_service_client.get_blob_client(container=container_name, blob= file_name)
        # print(container_client.get_container_access_policy())
        container_client.set_container_access_policy(signed_identifiers={},public_access="blob")

    #     print("does container exists",container_exists(blob_client),blob_client)
        
        # print(blob_client.url)
        # 
        # print("\nUploading to Azure Storage as blob:\n\t" + file_name)

        # with open(upload_file_path, "rb") as data:
        #     blob_client.upload_blob(data)
        # try:
        #     print(blob_client.url)
        #     print(type(blob_client))

        # except ResourceNotFoundError:
        #     print("Container not exist")

    # print("\nListing blobs...")

    # # List the blobs in the container
    # blob_list = container_client.list_blobs()
    # for blob in blob_list:
    #     print("\t" + blob.name)

except Exception as ex:
    print('Exception:')
    print(ex)