import React, { PureComponent } from "react";

import char_it_logo from "../../images/char_it_logo-1.png";
import "./HomeHeader.scss";

class HomeHeader extends PureComponent {
  render() {
    return (
      <div className="home-header-parent">
        <div className="header-logo">
          <a href="https://char-it.netlify.app">
            <img
              src={char_it_logo}
              alt="char-it"
              style={{ height: "47px", width: "57px" }}
            />
          </a>
        </div>
        <div className="home-header">Let's Characterize it !</div>
      </div>
    );
  }
}

export default HomeHeader;
