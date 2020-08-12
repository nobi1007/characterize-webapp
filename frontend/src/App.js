import React, { PureComponent } from "react";

import "./styles/scss/index.scss";
import HomePage from "./components/HomePage"

class App extends PureComponent {
  
  render() {
    return (
      <HomePage />
    );
  }
}

export default App;