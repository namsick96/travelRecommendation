let initialState = [];

function typeTest(state = initialState, action) {
  switch (action.type) {
    case "ADD_ANSWER":
      let copy = [...state];
      copy.push(action.payload);
      console.log(copy);
      return copy;
    default:
      return state;
  }
}

export default typeTest;
