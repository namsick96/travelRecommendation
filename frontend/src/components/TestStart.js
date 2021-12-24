import React from "react";
import { Link } from "react-router-dom";
import island from "../css/island.png";
import "../css/ts.css";

function TestStart() {
  return (
    <>
      <div>
        <h4 className="bar1">여기 올레</h4>
        <div className="testcont">
        <div className="cont">
        <h1 className="test4">#여행 유형 테스트</h1>
        <h3 className="question3">나는 어떤 여행가일까?</h3>
        <img className="island" src={island}></img><br></br>
        <button className="button6">
          <Link to="/test/1" style={{ textDecoration: 'none' , color: 'white'}}>  테스트 시작하기  </Link>
        </button>
        </div>
        </div>
      </div>
    </>
  );
}

export default TestStart;
