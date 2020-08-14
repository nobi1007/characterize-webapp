import React from "react";
import ReactDOM from "react-dom";
import * as serviceWorker from "./serviceWorker";
import App from "./App";
import {Provider} from "react-redux";
import configureStore from "./configureStore";



const ApolloApp = () => (
  <Provider store={configureStore()}>
    <App />
  </Provider>
);

ReactDOM.render(<ApolloApp/>, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();