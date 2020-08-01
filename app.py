from flask import Flask, render_template, request, redirect, url_for, jsonify
import flask_login
import os, json
from oauthlib.oauth2 import WebApplicationClient
import requests

app = Flask(__name__)
app.secret_key = "7y8gb87t76g878t6243rnd2wor8dj98"

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


## Google Login Configuration

GOOGLE_CLIENT_ID = "687219282230-e2lp5lfsp5pk7hrkfbnrhg93mctdv8jt.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "RnR64eA3H4ICcggbMjRDVc8W"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

## Mock Database 

users = {
    "Shyam":{
        "id" : "Shyam",
        "email" : "abc@gmail.com"  
    }
}

class User(flask_login.UserMixin):
    pass


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
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )

    return redirect(request_uri)


@app.route("/api/glogin/callback")
def callback():

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

@app.route("/home")
@app.route("/")
@flask_login.login_required
def protected():
    return render_template("index.html",user_id=flask_login.current_user.id)


@app.route('/logout', methods=["GET","POST"])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return '''
            Please <a href="/glogin">login</a> first! 
           '''

if __name__ == "__main__":
    app.run(port=8080, debug=True)