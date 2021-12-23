/* eslint-disable */
import axios from "axios";

let initialState = {
  // type: JSON.parse(localStorage.getItem("obj")).type,
  // score: JSON.parse(localStorage.getItem("obj")).score,
  src: { lat: 0, lng: 0 },
  dst: { lat: 0, lng: 0 },
  mvp: 0,
  result: {},
};

export const getResult = async (props) => {
  try {
    console.log("props");
    console.log(props);
    const data = JSON.stringify(props);
    console.log("data");
    console.log(data);
    const instance = axios.create({
      baseURL: "http://3.34.82.24:8080",
    });
    const finalResult = await instance
      .post("/final_result", data, {
        headers: { "Content-Type": "application/json" },
      })
      .then((response) => console.log(response)) // 받아온 결과값 변수에 저장해서 Result.js에 넘겨주기
      .catch((error) => console.log(error));

    return {
      type: "GET_FINALRESULT_SUCCESS",
      result: finalResult,
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
