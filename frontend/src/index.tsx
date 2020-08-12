import React, { useState } from "react";
import ReactDOM from "react-dom";
import * as serviceWorker from "./serviceWorker";
import { Router } from "react-router-dom";
import { createBrowserHistory } from "history";
import App from "./App";
import ReactGA from "react-ga";

const history = createBrowserHistory();

history.listen((location) => {
  // ReactGA.set({ page: location.hash }); // Update the user's current page
  // ReactGA.pageview(location.hash); // Record a pageview for the given page
});

const ApolloApp = (AppComponent: any) => (
  <Router history={history}>
    <AppComponent />
  </Router>
);

ReactDOM.render(ApolloApp(App), document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();