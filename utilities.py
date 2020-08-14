import os, json
import cv2
import numpy as np
import requests
from flask import render_template, redirect, url_for
import flask_login
from CustomFileStorage import *
from oauthlib.oauth2 import WebApplicationClient
from dotenv import load_dotenv
from random import shuffle

load_dotenv()

## Google Login Configuration

# GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
# GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
# GOOGLE_DISCOVERY_URL = (
#     "https://accounts.google.com/.well-known/openid-configuration"
# )

# client = WebApplicationClient(GOOGLE_CLIENT_ID)

def get_new_name():
    nums = list(range(97,123))
    chars = list(map(chr,nums))
    nos = list(range(1,10))
    shuffle(nos)
    shuffle(chars)
    return "".join(chars[:5]) + "".join(list(map(str,nos))[:3])

def handle_show_image(request):
    try:
        uploaded_file = request.files["input_image"].read()
    except:
        return "Invalid Request"

    input_file_name = get_new_name()
    input_user_id = "chard1open1id"
    npimg = np.fromstring(uploaded_file, np.uint8)
    input_file_data = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    storage_object = CustomFileStorage(user_id = input_user_id)
    
    storage_object.store_file(file_name = input_file_name, file_data = input_file_data, file_type = "image")
    image_uri = storage_object.saved_file_uri
    
    req_data = {
        "user_id":input_user_id,
        "file_uri":image_uri,
        "file_name":storage_object.file_name
    }

    response = requests.post(url="http://127.0.0.1:8080/api/characterizer101",json=req_data)
    
    return response.content

# def get_google_provider_cfg():
#     return requests.get(GOOGLE_DISCOVERY_URL).json()

# def handle_google_login_callback(request, User, users):
#     code = request.args.get("code")
#     google_provider_cfg = get_google_provider_cfg()
#     token_endpoint = google_provider_cfg["token_endpoint"]

#     # Prepare and send request to get tokens! Yay tokens!
#     token_url, headers, body = client.prepare_token_request(
#         token_endpoint,
#         authorization_response=request.url,
#         redirect_url=request.base_url,
#         code=code,
#     )

#     token_response = requests.post(
#         token_url,
#         headers=headers,
#         data=body,
#         auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
#     )


#     client.parse_request_body_response(json.dumps(token_response.json()))

#     # Now that we have tokens (yay) let's find and hit URL
#     # from Google that gives you user's profile information,
#     # including their Google Profile Image and Email
#     userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
#     uri, headers, body = client.add_token(userinfo_endpoint)
#     userinfo_response = requests.get(uri, headers=headers, data=body)

#     # We want to make sure their email is verified.
#     # The user authenticated with Google, authorized our
#     # app, and now we've verified their email through Google!
#     if userinfo_response.json().get("email_verified"):
#         unique_id = userinfo_response.json()["sub"]
#         users_email = userinfo_response.json()["email"]
#         picture = userinfo_response.json()["picture"]
#         users_name = userinfo_response.json()["given_name"]
#     else:
#         return "User email not available or not verified by Google.", 400

#     # Create a user in our db with the information provided
#     # by Google
#     user = User()
#     user.id = users_name

#     # Doesn't exist? Add to database
#     if not users_name in users:
#         users[users_name] = {
#             "name":users_name,
#             "email":users_email
#         }

#     # Begin user session by logging the user in
#     flask_login.login_user(user)

#     # Send user back to homepage
#     return redirect(url_for("protected"))

def array3T2(array):
    ans = []
    for i in range(len(array)):
        temp = []
        for j in range(len(array[0])):
            temp.append(sum(array[i][j])//3)
        ans.append(temp)
    return ans.copy()


def characterize101(image_data:np.ndarray) -> str:

    characters = list("@#&S`%+-. ")

    cv2.imwrite("sample_image.png",image_data)
    array_x = cv2.imread("sample_image.png",0)
    os.remove("sample_image.png")

    height = 40
    factor = (len(array_x)//height)//2
    width = len(array_x[0])//factor

    resized_image = cv2.resize(array_x,(width,height))

    output_data = ""

    for i in range(height):
        for j in range(width):
            if 0 <= resized_image[i][j] <= 26:
                output_data += characters[0]
            elif 27 <= resized_image[i][j] <= 52:
                output_data += characters[1]
            elif 53 <= resized_image[i][j] <= 78:
                output_data += characters[2]
            elif 79 <= resized_image[i][j] <= 104:
                output_data += characters[3]
            elif 105 <= resized_image[i][j] <= 130:
                output_data += characters[4]
            elif 131 <= resized_image[i][j] <= 156:
                output_data += characters[5]
            elif 157 <= resized_image[i][j] <= 182:
                output_data += characters[6]
            elif 183 <= resized_image[i][j] <= 206:
                output_data += characters[7]
            elif 207 <= resized_image[i][j] <= 230:
                output_data += characters[8]
            elif 231 <= resized_image[i][j] <= 255:
                output_data += characters[9]
        output_data += "\n"

    return output_data