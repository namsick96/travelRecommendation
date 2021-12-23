/* eslint-disable */
import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getTypeResult } from "../reducers/typeResult";

function TypeResult() {
  let [loading, setLoading] = useState(true);
  let [showResult, setShowResult] = useState(false);
  let state = useSelector((state) => state.typeResult);
  console.log("state");
  console.log(state);
  let dispatch = useDispatch();

  useEffect(() => {
    // 컴포넌트 첫 렌더링 시 서버에 유형 결과 요청해서 받아오는 코드
    getTypeResult().then((result) => {
      dispatch(result);
      setLoading(false);
      setShowResult(true);
    });
  }, []);
  console.log("data:");
  console.log(state.data);

  return (
    <>
      {/* 요청 성공하면 결과를 화면에 보여주는 코드 */}
      {loading === true ? <Loading></Loading> : null}
      {showResult === true ? <Result data={state.data}></Result> : null}
    </>
  );
}

function Loading() {
  return <div>로딩 중</div>;
}

function Result(props) {
  return <div>{props.data.userId}</div>;
}
export default TypeResult;
