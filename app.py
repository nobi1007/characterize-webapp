from flask import Flask, render_template, request, redirect, url_for, jsonify
import flask_login
import os, json
from oauthlib.oauth2 import WebApplicationClient
import requests
import cv2
import numpy
from utilities import *
from dotenv import load_dotenv
from CustomFileStorage import *

load_dotenv()

app = Flask(__name__)
app.secret_key = "7y8gb87t76g878t6243rnd2wor8dj98"

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

## Mock Database 

users = {
    "Shyam":{
        "id" : "Shyam",
        "email" : "abc@gmail.com"  
    }
}

class User(flask_login.UserMixin):
    pass


## ------------------------------ Login Handler ----------------------------

@login_manager.user_loader
def user_loader(name):
    if name not in users:
        return

    user = User()
    user.id = name
    return user


@login_manager.request_loader
def request_loader(request):
    name = request.form.get("name")
    if name not in users:
        return
    user = User()
    user.id = name
    user.is_authenticated = request.form["email"] == users[name]["email"]
    return user

@app.route("/glogin")
def google_login():

    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri = request.base_url[:-7] + "/api/glogin/callback",
        scope=["openid", "email", "profile"],
    )

    return redirect(request_uri)


@app.route("/api/glogin/callback")
def callback():
    return handle_google_login_callback(request, User, users)

## ------------------------------------- Logout Handler -----------------------------------

@app.route('/logout', methods=["GET","POST"])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return 'Logged out'


## ------------------------------------- Home/Dashboard -------------------------------------

@app.route("/home")
@app.route("/")
@flask_login.login_required
def protected():
    return render_template("index.html",user_id=flask_login.current_user.id)


## ------------------------------------- API - Characterizer -------------------------------------

@app.route("/api/characterizer101", methods = ["POST"])
def characterizerV101():
    req = request.get_json()
    user_id = req["user_id"]
    file_uri = req["file_uri"]
    original_file_name = req["file_name"]

    file_response = requests.get(file_uri)
    npimg = np.fromstring(file_response.content, np.uint8)
    request_file_data = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    chard_image_data = characterize101(request_file_data)

    file_object = CustomFileStorage(user_id = user_id)
    file_object.store_file(file_name = "chard-101-" + original_file_name, file_data = chard_image_data, file_type="text")    
    characterized_image_uri = file_object.saved_file_uri
    
    return {
        "characterized-image-uri":characterized_image_uri
    }


@app.route("/show_image",methods=["GET","POST"])
def displayImage():
    if request.method == "GET":
        return render_template("display_image.html")
    else:
        return handle_show_image(request)
        
        
## ------------------------------------- Unauthorized Handler -------------------------------------

@login_manager.unauthorized_handler
def unauthorized_handler():

    return '''
            Please <a href="/glogin">login</a> first! 
        '''

@app.route("/checker",methods=["POST"])
def checker():
    req = request.get_json()
    print("this is key-val","a -",req["a"])
    print("Just checking",req)
    return {
        "x":"y"
    }


if __name__ == "__main__":
    app.run(port=8080, debug=True)