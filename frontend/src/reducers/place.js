/* eslint-disable */
import axios from "axios";

let initialState = {
  type: 0,
  scores: {},
  starting: { lat: 0, lng: 0 },
  destination: { lat: 0, lng: 0 },
  mvp: 0,
  result: {},
};

export const getResult = async (props) => {
  try {
    const data = JSON.stringify(props);
    console.log("data");
    console.log(data);
    const instance = axios.create({
      baseURL: "http://3.34.82.24:8080",
    });
    const finalResult = await instance.post("/final_result", data, {
      headers: { "Content-Type": "application/json" },
    });
    console.log(finalResult.data);
    return {
      type: "GET_FINALRESULT_SUCCESS",
      result: finalResult.data,
    };
  } catch (e) {
    return {
      type: "GET_FINALRESULT_FAILURE",
    };
  }
};

function place(state = initialState, action) {
  switch (action.type) {
    case "ADD_USER_INFO":
      console.log("userinfo dispatch happend!");
      return {
        ...state,
        type: action.testType,
        scores: action.scores,
      };
    case "ADD_SRC":
      console.log("src dispatch happend!");
      console.log({ ...state, starting: { lat: action.lat, lng: action.lng } });
      return {
        ...state,
        starting: { lat: action.lat, lng: action.lng },
      };
    case "ADD_DST":
      console.log("dst dispatch happend!");
      console.log({
        ...state,
        destination: { lat: action.lat, lng: action.lng },
      });
      return {
        ...state,
        destination: { lat: action.lat, lng: action.lng },
      };
    case "ADD_MVP":
      console.log("mvp dispatch happend!");
      console.log({ ...state, mvp: action.key });
      return {
        ...state,
        mvp: action.key,
      };
    case "GET_FINALRESULT_SUCCESS":
      console.log("succeed");
      console.log({...state, result:action.result});
      return {
        ...state,
        result: action.result,
      };
    case "GET_FINALRESULT_FAILURE":
      console.log("failed");
      return state;
    default:
      return state;
  }
}

export default place;
