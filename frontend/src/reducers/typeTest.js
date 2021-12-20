import axios from "axios";

let initialState = [];

function typeTest(state = initialState, action) {
  switch (action.type) {
    case "ADD_ANSWER":
      let copy = [...state];
      copy.push(action.payload);
      console.log(copy);
      return copy;
    case "POST_ANSWER":
      console.log("post요청 발생");
      console.log("요청 시 state값");
      console.log(state);
      axios
        .post("127.0.0.1:8080/type_result", state)
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
      return state;
    default:
      return state;
  }
}

export default typeTest;
