/* eslint-disable */
import axios from "axios";

export const getTypeResult = async () => {
  // action객체를 뱉어내는 thunk함수
  try {
    const typeResult = await axios.get(
      "https://jsonplaceholder.typicode.com/todos/2"
    );
    console.log("api 요청 결과");
    console.log(typeResult);
    return {
      type: "GET_RESULT_SUCCESS",
      result: typeResult.data,
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
      return {
        ...state,
        error: action.error,
      };
    default:
      return state;
  }
}

export default typeResult;
