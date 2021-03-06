/* eslint-disable */

import React, { useState,useEffect } from "react";
import { useParams, useHistory, Link, Route } from "react-router-dom";
import Questions from "../data/questions";
import { useSelector, useDispatch } from "react-redux";
import "../css/Type.css";
import font from "../font/font.css";

function GetType() {
  let { id } = useParams();
  let found = Questions.find((x) => x.id == id);
  let history = useHistory();
  let dispatch = useDispatch();
  let [answer, setAnswer] = useState(-1);

  return (
    <>
      <div className="content">
        <h4 className="bar" style={{fontFamily : 'WandohopeR'}}>여기 올레</h4>
        <div className="container">
        <h2 className="num">Q{id}.</h2>
        <h3 className="question">{found.question}</h3>
        </div>
        {found.answer.map((a, i) => {
          return (
            <div key={i}>
              <button className="selection selection2" 
                onClick={() => {
                  setAnswer(i);
                }}
                style={i===answer ? { background:'#F4A644'} : null}
              >
                {a}
              </button>
              <br></br>
            </div>
          );
        })}
      </div>
      {id != 0 ? (
        <button className="back button2"
          onClick={() => {
            history.goBack();
          }}
        >
          이전으로
        </button>
      ) : null}

      {id != 10 ? (
        <button className="next button3"
          onClick={() => {
            // 문항별 응답 store에 저장
            dispatch({ type: "ADD_ANSWER", payload: found.result[answer] }); // found 중 사용자가 고른 선지에 해당하는 r값을 전송
          }}
        >
          <Link to={`/test/${parseInt(id) + 1}`} style={{ textDecoration: 'none' , color: 'white'}}>다음으로</Link>
        </button>
      ) : null}
      {id == 10 ? (
        <button className="next button3"
          onClick={() => {
            // 12번 응답 저장 후 백엔드 서버에 최종 응답 전송
            dispatch({ type: "ADD_ANSWER", payload: found.result[answer] });
            // dispatch({ type: "POST_ANSWER" });
          }}
        >
          <Link to="/testresult" style={{ textDecoration: 'none' , color: 'white'}}>제출하기</Link>
        </button>
      ) : null}
    </>
  );
}
export default GetType;
