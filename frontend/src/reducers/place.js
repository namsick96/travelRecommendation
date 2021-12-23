/* eslint-disable */
import axios from "axios";

let temp = JSON.parse(localStorage.getItem("obj"));

let initialState = {
  type: temp.type,
  scores: temp.scores,
  src: { lat: 0, lng: 0 },
  dst: { lat: 0, lng: 0 },
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
    case "ADD_SRC":
      console.log("src dispatch happend!");
      console.log({ ...state, src: { lat: action.lat, lng: action.lng } });
      return {
        ...state,
        src: { lat: action.lat, lng: action.lng },
      };
    case "ADD_DST":
      console.log("dst dispatch happend!");
      console.log({ ...state, dst: { lat: action.lat, lng: action.lng } });
      return {
        ...state,
        dst: { lat: action.lat, lng: action.lng },
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
