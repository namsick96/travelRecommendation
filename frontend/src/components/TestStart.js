import React from "react";
import { Link } from "react-router-dom";
import island from "../css/island.png";
import "../css/ts.css";
import font from "../font/font.css";

function TestStart() {
  return (
    <>
      <div>
        <h4 className="bar1" style={{fontFamily : 'WandohopeR'}}>여기 올레</h4>
        <div className="testcont">
        <div className="cont">
        <h1 className="test4" style={{fontFamily: 'EliceDigitalBaeum_Bold'}}>#여행 유형 테스트</h1>
        <h3 className="question3" style={{fontFamily: 'Cafe24SsurroundAir'}}>나는 어떤 여행가일까?</h3>
        <img className="island" src={island}></img><br></br>
        <button className="button6">
          <Link to="/test/1" style={{ textDecoration: 'none' , color: 'white', fontFamily: 'Cafe24SsurroundAir'}}>  테스트 시작하기  </Link>
        </button>
        </div>
        </div>
      </div>
    </>
  );
}

export default TestStart;
