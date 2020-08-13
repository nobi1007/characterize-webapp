import React, { PureComponent } from "react";
import GoogleLogin from 'react-google-login';
import "./HomePage.scss";


class HomePage extends PureComponent{

    // successResponseGoogle = (response) => {
    //     console.log("success ",response);
    // }

    // failureResponseGoogle = (response) => {
    //     console.log("failure ",response);
    // } 

    render(){
        return(
            <div>
                <div>Hello Shyam</div>
                
                <div>
                    {/* Lets handle auth later */}
                    {/* <GoogleLogin
                        clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}
                        buttonText="Login with Google"
                        onSuccess={this.successResponseGoogle}
                        onFailure={this.failureResponseGoogle}
                        cookiePolicy={'single_host_origin'}
                        isSignedIn={true}
                    /> */}
                </div>

            </div>
        )
    }
}

export default HomePage;