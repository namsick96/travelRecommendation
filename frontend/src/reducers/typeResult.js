/* eslint-disable */
import axios from "axios";

const initialState = {
  input: [],
  result: null,
  status: null,
};
export const getTypeResult = async (props) => {
  // action객체를 뱉어내는 thunk함수

  try {
    const data = JSON.stringify({ answer: props });
    const instance = axios.create({
      baseURL: "http://3.34.82.24:8080",
    });
    const typeResult = await instance // 데이터를 전송한 다음 받은 유형 정보가 담기는 변수
      .post("/type_result", data, {
        headers: { "Content-Type": "application/json" },
      });
    console.log(typeResult.data);
    return {
      type: "GET_TYPERESULT_SUCCESS",
      payload: typeResult.data,
      status: true,
    };
  } catch (e) {
    return {
      type: "GET_TYPERESULT_FAILURE",
      status: false, 
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
    case "GET_TYPERESULT_PENDING":
      return {
        ...state,
        status: false,
      };
    case "GET_TYPERESULT_SUCCESS":
      console.log("payload");
      console.log(action.payload);
      return {
        ...state,
        status: true,
        result: action.payload,
      };
    case "GET_TYPERESULT_FAILURE":
      return {
        ...state,
        status: false,
      };
    default:
      return state;
  }
}

export default typeResult;
