import React from "react";
import { Link } from "react-router-dom";

function TestStart() {
  return (
    <>
      <div>
        <h1>여행 유형 테스트</h1>
        <h3>나는 어떤 여행가일까?</h3>
        <button>
          <Link to="/test/1">테스트 시작하기</Link>
        </button>
      </div>
    </>
  );
}

export default TestStart;
