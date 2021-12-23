/* eslint-disable */

import React, { useState } from "react";
import { useParams, useHistory, Link, Route } from "react-router-dom";
import Questions from "../data/questions";
import { useSelector, useDispatch } from "react-redux";

function GetType() {
  let { id } = useParams();
  let found = Questions.find((x) => x.id == id);
  let history = useHistory();
  let dispatch = useDispatch();
  let [answer, setAnswer] = useState(0);

  return (
    <>
      <div className="content">
        <h3>{found.question}</h3>
        {found.answer.map((a, i) => {
          return (
            <div key={i}>
              <button
                onClick={() => {
                  setAnswer(i);
                }}
              >
                {a}
              </button>
              <br></br>
            </div>
          );
        })}
      </div>
      {id != 0 ? (
        <button
          onClick={() => {
            history.goBack();
          }}
        >
          뒤로가기
        </button>
      ) : null}

      {id != 12 ? (
        <button
          onClick={() => {
            // 문항별 응답 store에 저장
            dispatch({ type: "ADD_ANSWER", payload: found.result[answer] }); // found 중 사용자가 고른 선지에 해당하는 r값을 전송
          }}
        >
          <Link to={`/test/${parseInt(id) + 1}`}>다음 문제</Link>
        </button>
      ) : null}
      {id == 12 ? (
        <button
          onClick={() => {
            // 12번 응답 저장 후 백엔드 서버에 최종 응답 전송
            dispatch({ type: "ADD_ANSWER", payload: found.result[answer] });
            // dispatch({ type: "POST_ANSWER" });
          }}
        >
          <Link to="/testresult">제출하기</Link>
        </button>
      ) : null}
    </>
  );
}
export default GetType;
