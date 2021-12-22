/* eslint-disable */

import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getResult } from "../reducers/place";

function Result() {
  let [loading, setLoading] = useState(true);
  let [showResult, setShowResult] = useState(false);
  let state = useSelector((state) => state);

  let dispatch = useDispatch();

  useEffect(() => {
    getResult().then((result) => {
      dispatch(result);
      setLoading(false);
      setShowResult(true);
    });
  }, []);
  return;
  <>
    {/* 요청 성공하면 결과를 화면에 보여주는 코드 */}
    {loading === true ? <Loading></Loading> : null}
    {showResult === true ? (
      <ResultComponent data={state.data}></ResultComponent>
    ) : null}
  </>;
}

function Loading() {
  return <div>로딩 중</div>;
}

function ResultComponent(props) {
  return (
    <div>
      <p>test</p>
      {/* {props.data.type} */}
    </div>
  );
}

export default Result;
