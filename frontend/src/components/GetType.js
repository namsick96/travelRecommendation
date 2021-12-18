/* eslint-disable */

import React, { useState } from "react";
import { useParams, useHistory, Link, Route } from "react-router-dom";
import Questions from "../questions";

function GetType() {
  let { id } = useParams();
  let found = Questions.find((x) => x.id == id);
  let history = useHistory();

  return (
    <>
      <div className="content">
        <h3>{found.question}</h3>
        <p>{found.a1}</p>
        <p>{found.a2}</p>
        <p>{found.a3}</p>
        <p>{found.a4}</p>
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
          }}
        >
          <Link to={`/test/${parseInt(id) + 1}`}>다음 문제</Link>
        </button>
      ) : null}
      {id == 12 ? (
        <button
          onClick={() => {
            // 12번 응답 저장 후 백엔드 서버에 최종 응답 전송
          }}
        >
          제출하기
        </button>
      ) : null}
    </>
  );
}
export default GetType;
