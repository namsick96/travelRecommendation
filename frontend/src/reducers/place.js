/* eslint-disable */
import axios from "axios";

let initialState = {
  type: "",
  src: { lat: 0, lng: 0 },
  dst: { lat: 0, lng: 0 },
  mvp: 0,
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
    case "POST_PLACES":
      axios
        .post("3.34.82.24:8080/final_result", state)
        .then((response) => console.log(response))
        .catch((error) => console.log(error));
    default:
      return state;
  }
}

export default place;
