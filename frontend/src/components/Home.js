import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <>
      <div>
        <h1>여기올레</h1>
        <h3>당신을 위한 여행 코스 추천 서비스</h3>
        <button>
          <Link>여행 유형 테스트하고 여행 코스 추천 받기</Link>
        </button>
      </div>
    </>
  );
}

export default Home;
