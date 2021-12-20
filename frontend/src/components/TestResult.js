/* eslint-disable */
import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getTypeResult } from "../reducers/typeResult";

function TypeResult() {
  let [loading, setLoading] = useState(true);
  let state = useSelector((state) => state.typeResult);
  console.log("state");
  console.log(state);
  let dispatch = useDispatch();

  useEffect(() => {
    // 컴포넌트 첫 렌더링 시 서버에 유형 결과 요청해서 받아오는 코드
    getTypeResult().then((result) => {
      dispatch(result);
      setLoading(false);
    });
  }, []);
  console.log("data:");
  console.log(state.data);

  const result = [state.data] ?? [];
  console.log("result:");
  console.log(result);

  return (
    <>
      {/* 요청 성공하면 결과를 화면에 보여주는 코드 */}
      {loading === true ? <Loading></Loading> : null}
      {loading === false ? <button>결과보기</button> : null}
      <div>hey {result.userId}</div>
    </>
  );
}

function Loading() {
  return <div>로딩 중</div>;
}
export default TypeResult;
