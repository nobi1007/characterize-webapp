import ReactGA from "react-ga";

const trackingId = "UA-128624564-3";

export const initializeGA = () => {
  ReactGA.initialize(trackingId);
  console.log("Initialize GA getting called");
  ReactGA.set({
    userId: "testUserId",
  });
};
