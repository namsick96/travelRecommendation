let initialState = [];

function testReducer(state = initialState, action) {
  if (action.type === "ADD_ANSWER") {
    let copy = [...state];
    copy.push(action.payload);
    return copy;
  } else return state;
}

export default testReducer;
