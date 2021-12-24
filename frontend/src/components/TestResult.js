/* eslint-disable */
import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getTypeResult } from "../reducers/typeResult";
import typeInfo from "../data/typeInfo";
import { Link } from "react-router-dom";
import "../css/tr.css";
import jeju from "../css/jeju.png";
import font from "../font/font.css";

function TypeResult() {
  let [loading, setLoading] = useState(true);
  let [showButton, setShowButton] = useState(false);
  let [showResult, setShowResult] = useState(false);
  let state = useSelector((state) => state);

  let dispatch = useDispatch();

  useEffect(() => {
    // 컴포넌트 첫 렌더링 시 서버에 유형 결과 요청해서 받아오는 코드
    getTypeResult(state.typeResult.input).then((result) => {
      dispatch(result);
      setShowButton(result.status);
    });
  }, []);

  return (
    <>
       <h4 className="bar1" style={{fontFamily : 'WandohopeR'}}>여기 올레</h4>
       <div className="testcont">
      <div className="cont">
      {/* 요청 성공하면 결과를 화면에 보여주는 코드 */}
      {loading === true ? <Loading></Loading> : null}
      {showButton === true ? (
        <button className="button7" style={{fontFamily: 'Cafe24SsurroundAir'}}
          onClick={() => {
            setLoading(false);
            setShowButton(false);
            setShowResult(true);
          }}
        >
          나의 여행 유형 확인하기
        </button>
      ) : null}
      {showResult === true ? (
        <Result
          dispatch={dispatch}
          data={typeInfo[state.typeResult.result.type]}
          state={state}
        ></Result>
      ) : null}
      </div></div>
    </>
  );
}

function Loading() {
  return (
  <div>
  <h1 className="hashtag">#</h1>
  <div className="loading" style={{fontFamily: 'EliceDigitalBaeum_Bold'}}>테스트 결과 로딩 중</div>
  <img className="jihoon" src={jeju}></img>
  </div>
  )
}

function Result(props) {
  console.log("props");
  console.log(props);
  return (
    <div className="">
      <h2 className="type" style={{fontFamily: 'EliceDigitalBaeum_Bold'}}> 당신의 유형은</h2> 
      <h1 className="name" style={{ fontFamily: 'paybooc-Bold'}}>{props.data.title}</h1>
      <h4 className="hashtaging" style={{ fontFamily: 'paybooc-Bold'}}>{props.data.hashtag}</h4>
      <p className="des" style={{ fontFamily: 'paybooc-Bold'}}>{props.data.description}</p>
      <button className="button10">
        <Link  style={{ textDecoration: 'none' , color: 'white', fontFamily: 'Cafe24SsurroundAir'}}
          onClick={() => {
            props.dispatch({
              type: "ADD_USER_INFO",
              testType: props.state.typeResult.result.type,
              scores: props.state.typeResult.result.scores,
            });
          }}
          to="/src"
        >
          여행코스 추천받기
        </Link>
      </button>
    </div>

  );
}
export default TypeResult;
