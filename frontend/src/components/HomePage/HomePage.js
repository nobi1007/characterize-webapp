import React, { PureComponent } from "react";
// import GoogleLogin from 'react-google-login';
import "./HomePage.scss";

import HomeHeader from "../HomeHeader";
import HomeBody from "../HomeBody";
import HomeFooter from "../HomeFooter";

class HomePage extends PureComponent {
  render() {
    return (
      <div className="home-page">
        <HomeHeader />
        <HomeBody />
        <HomeFooter />
      </div>
    );
  }
}

export default HomePage;
