/* eslint-disable */
import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getTypeResult } from "../reducers/typeResult";
import typeInfo from "../data/typeInfo";
import { Link } from "react-router-dom";

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
      {/* 요청 성공하면 결과를 화면에 보여주는 코드 */}
      {loading === true ? <Loading></Loading> : null}
      {showButton === true ? (
        <button
          onClick={() => {
            setLoading(false);
            setShowButton(false);
            setShowResult(true);
          }}
        >
          결과 보기
        </button>
      ) : null}
      {showResult === true ? (
        <Result
          data={typeInfo[state.typeResult.result.type]}
          dispatch={dispatch}
          state={state}
        ></Result>
      ) : null}
    </>
  );
}

function Loading() {
  return <div>로딩 중</div>;
}

function Result(props) {
  return (
    <div>
      <h1>{props.data.title}</h1>
      <p>{props.data.description}</p>
      <button>
        <Link
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
