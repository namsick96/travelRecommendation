/* eslint-disable */
import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getTypeResult } from "../reducers/typeResult";
import typeInfo from "../data/typeInfo";

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
      setShowButton(true);
    });
  }, []);

  return (
    <>
      {/* 요청 성공하면 결과를 화면에 보여주는 코드 */}
      {loading === true ? (
        <Loading>
          {showButton === true ? (
            <button
              onClick={() => {
                setLoading(false);
                setShowResult(true);
              }}
            >
              나의 여행 유형 확인하기
            </button>
          ) : null}
        </Loading>
      ) : null}
      {showResult === true ? (
        <Result data={typeInfo[state.typeResult.result]}></Result>
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
        <Link to="/src">여행코스 추천받기</Link>
      </button>
    </div>
  );
}
export default TypeResult;
