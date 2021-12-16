/* eslint-disable */

import "./App.css";
import GetPlace from "./components/GetPlace.js";
import GetType from "./components/GetType";
import Result from "./components/Result";
import Home from "./components/Home";
import { Link, Route, Switch } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <p>nav</p>
      <Switch>
        <Route exact path="/" component={Home}></Route>
        <Route path="/test" component={GetType}></Route>
        <Route path="/place" component={GetPlace}></Route>
        <Route path="/result" component={Result}></Route>
      </Switch>
    </div>
  );
}

export default App;
