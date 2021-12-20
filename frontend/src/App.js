/* eslint-disable */

import "./App.css";
import GetPlace from "./components/GetPlace.js";
import GetType from "./components/GetType";
import Result from "./components/Result";
import Home from "./components/Home";
import { Link, Route, Switch } from "react-router-dom";
import TestResult from "./components/TestResult";

function App() {
  return (
    <div className="App">
      <h2>navbar</h2>
      <Switch>
        <Route exact path="/" component={Home}></Route>
        <Route path="/test/:id" component={GetType}></Route>
        <Route exact path="/testresult" component={TestResult}></Route>
        <Route path="/place" component={GetPlace}></Route>
        <Route path="/result" component={Result}></Route>
      </Switch>
    </div>
  );
}

export default App;
