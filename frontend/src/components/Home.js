/* eslint-disable */
import React from "react";
import { Link } from "react-router-dom";
import "../css/Home.css";
import airplane from "../css/send.png";
import jeju from "../css/jeju.png";

function Home() {
  return (
    <>
      <div className="homecont">
        <div className="titlecont">
          <img src={airplane} className="airplane"></img>
          <h1 className="jejutitle">여기올레</h1>
          <h3 className="service">당신을 위한 여행 코스 추천 서비스</h3>
          <button className="tr button3">
            <Link
              to="/teststart"
              style={{ textDecoration: "none", color: "white" }}
            >
              여행 유형 테스트하고 여행 코스 추천 받기
            </Link>
          </button>
        </div>
        <img src={jeju} className="jeju"></img>
      </div>
    </>
  );
}

export default Home;
