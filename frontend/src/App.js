/* eslint-disable */

import "./App.css";
import GetType from "./components/GetType";
import Result from "./components/Result";
import Home from "./components/Home";
import { Link, Route, Switch } from "react-router-dom";
import TestResult from "./components/TestResult";
import TestStart from "./components/TestStart";
import GetSrc from "./components/GetSrc";
import GetDst from "./components/GetDst";
import GetMvp from "./components/GetMvp";
import { useEffect } from "react";

function App() {
  useEffect(() => {
    localStorage.setItem("obj", { type: 0, scores: {} });
  }, []);
  return (
    <div className="App">
      <Switch>
        <Route exact path="/" component={Home}></Route>
        <Route path="/teststart" component={TestStart}></Route>
        <Route path="/test/:id" component={GetType}></Route>
        <Route exact path="/testresult" component={TestResult}></Route>
        <Route path="/src" component={GetSrc}></Route>
        <Route path="/mvp" component={GetMvp}></Route>
        <Route path="/dst" component={GetDst}></Route>
        <Route path="/result" component={Result}></Route>
      </Switch>
    </div>
  );
}

export default App;
