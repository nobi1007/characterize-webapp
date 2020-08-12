import os, json
import cv2
import numpy as np
import requests
from flask import render_template, redirect, url_for
import flask_login
from CustomFileStorage import *
from oauthlib.oauth2 import WebApplicationClient

## Google Login Configuration

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)


def handle_show_image(request):
    try:
        uploaded_file = request.files["input_image"].read()
    except:
        return "Invalid Request"

    input_file_name = str(request.form["file_name"])
    input_user_id = str(request.form["user_id"])
    npimg = np.fromstring(uploaded_file, np.uint8)
    input_file_data = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    
    storage_object = CustomFileStorage(user_id = input_user_id)
    
    storage_object.store_file(file_name = input_file_name, file_data = input_file_data)
    image_uri = storage_object.saved_file_uri
    
    return render_template("display_image.html",uploaded_image=image_uri)


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

def handle_google_login_callback(request, User, users):
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )


    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens (yay) let's find and hit URL
    # from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, authorized our
    # app, and now we've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in our db with the information provided
    # by Google
    user = User()
    user.id = users_name

    # Doesn't exist? Add to database
    if not users_name in users:
        users[users_name] = {
            "name":users_name,
            "email":users_email
        }

    # Begin user session by logging the user in
    flask_login.login_user(user)

    # Send user back to homepage
    return redirect(url_for("protected"))