import React, { PureComponent } from "react";

import "./HomeFooter.scss";
import heartIcon from "../../images/heart.png";

class HomeFooter extends PureComponent {
  render() {
    return (
      <div className="home-footer">
        !! Made with{" "}
        <img className="footer-heart-icon" src={heartIcon} alt="heart" /> by{" "}
        <a href="https://github.com/nobi1007">nobi1007</a> !!
      </div>
    );
  }
}

export default HomeFooter;
