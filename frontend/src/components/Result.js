/* eslint-disable */

import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getResult } from "../reducers/place";
import font from "../font/font.css";

function Result() {
  let [loading, setLoading] = useState(true);
  let [showResult, setShowResult] = useState(false);
  let state = useSelector((state) => state);

  let dispatch = useDispatch();

  useEffect(() => {
    getResult(state.place).then((result) => {
      dispatch(result);
      setLoading(false);
      setShowResult(true);
    });
  }, []);

  return (
    <>
      <p>최종 결과 페이지</p>
      {loading === true ? <Loading></Loading> : null}
      {showResult === true ? (
        <ResultComponent data={state}></ResultComponent>
      ) : null}
    </>
  );
}

function Loading() {
  return <div>로딩 중</div>;
}

function ResultComponent(props) {
  console.log("props");
  console.log(props.data);
  return (
    <div>
      <p>test</p>
      {/* {props.data.type} */}
    </div>
  );
}

export default Result;
