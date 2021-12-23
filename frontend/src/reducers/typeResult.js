/* eslint-disable */
import axios from "axios";

const initialState = {
  input: [],
  result: 0,
  score: {},
  error: "",
};
export const getTypeResult = async (props) => {
  // action객체를 뱉어내는 thunk함수
  try {
    console.log("props");
    console.log(props);
    const data = JSON.stringify({ answer: props }); // 이 시점에 state.data에 뭐가 들어있지?

    const instance = axios.create({
      baseURL: "http://3.34.82.24:8080",
    });
    console.log("data");
    console.log(data);
    const typeResult = await instance // 데이터를 전송한 다음 받은 유형 정보가 담기는 변수
      .post("/type_result", data, {
        headers: { "Content-Type": "application/json" },
      })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
    return {
      type: "GET_TYPERESULT_SUCCESS",
      result: typeResult,
    };
  } catch (e) {
    return {
      type: "GET_TYPERESULT_FAILURE",
      error: e,
    };
  }
};

function typeResult(state = initialState, action) {
  switch (action.type) {
    case "ADD_ANSWER":
      let copy = { ...state };
      copy.input.push(action.payload);
      console.log(copy);
      return copy;
    case "GET_TYPERESULT_SUCCESS":
      console.log("succeed");
      console.log(action.result);
      return {
        ...state,
        result: action.result,
      };
    case "GET_TYPERESULT_FAILURE":
      console.log("failed");
      console.log(action.error);
      return {
        ...state,
        error: action.error,
      };
    default:
      return state;
  }
}

export default typeResult;
