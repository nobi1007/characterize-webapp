import React, { PureComponent } from "react";
import GoogleLogin from 'react-google-login';

import "./HomePage.scss";

class HomePage extends PureComponent{

    responseGoogle = (response) => {
        console.log(response);
    }

    render(){
        console.log(process.env)
        return(
            <div>
                <div>Hello Shyam</div>
                <div>
                    <GoogleLogin
                    clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}
                    buttonText="Login"
                    onSuccess={this.responseGoogle}
                    onFailure={this.responseGoogle}
                    cookiePolicy={'single_host_origin'}
                    />
                </div>

            </div>
        )
    }
}

export default HomePage;