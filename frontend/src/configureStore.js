import { createStore, applyMiddleware, compose, combineReducers } from "redux";
import reducers from "./reducers";
import thunk from "redux-thunk";
function configureStore() {
  const enhancers = compose(
    // Middleware store enhancer.
    applyMiddleware(
      //apolloClient.middleware(),
      thunk
    ),
    // Redux Dev Tools store enhancer.
    // @see https://github.com/zalmoxisus/redux-devtools-extension
    // We only want this enhancer enabled for development and when in a browser
    // with the extension installed.
    process.env.NODE_ENV === "development" &&
      typeof window !== "undefined" &&
      (window).__REDUX_DEVTOOLS_EXTENSION__ &&
      (window).__REDUX_DEVTOOLS_EXTENSION__()
  );
  const store = createStore(
    combineReducers(
      Object.assign(
        {},
        // The application reducers.
        reducers
      )
      
    ),
    enhancers
  );
  if (process.env.NODE_ENV === "development" && (module).hot) {
    // Enable Webpack hot module replacement for reducers. This is so that we
    // don't lose all of our current application state during hot reloading.
    (module).hot.accept("./reducers", () => {
      // eslint-disable-next-line global-require
      const nextRootReducer = require("./reducers").default;

      store.replaceReducer(nextRootReducer);
    });
  }

  return store;
}
export default configureStore;
