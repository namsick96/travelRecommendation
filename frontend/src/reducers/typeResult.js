/* eslint-disable */
import axios from "axios";

export const getTypeResult = async (state) => {
  // action객체를 뱉어내는 thunk함수
  try {
    const instance = axios.create({
      baseURL: "https://3.34.82.24:8080",
    });
    const typeResult = await instance
      .post("/type_result", JSON.stringify({ answer: { ...state } }))
      .then((response) => console.log(response))
      .catch((error) => {
        console.log(error);
      });
    return {
      type: "GET_RESULT_SUCCESS",
      result: typeResult.type,
    };
  } catch (e) {
    return {
      type: "GET_RESULT_FAILURE",
      error: e,
    };
  }
};

const initialState = {
  loading: false,
  data: null,
  error: null,
};

function typeResult(state = initialState, action) {
  switch (action.type) {
    case "GET_RESULT":
      return {
        ...state,
        loading: true,
      };
    case "GET_RESULT_SUCCESS":
      console.log("succeed");
      return {
        ...state,
        data: action.result,
      };
    case "GET_RESULT_FAILURE":
      console.log("failed");
      console.log({ ...state, error: action.error });
      return {
        ...state,
        error: action.error,
      };
    default:
      return state;
  }
}

export default typeResult;
