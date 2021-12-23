import React from "react";
import Map from "./Map";
import "../css/Map.css";

function GetDst() {
  const type = "DST";
  return (
    <>
      <h3 className="bar1">여기올레</h3>
      <div className="container1">
      <h1 className="sug">당신의 도착지를 선택해주세요</h1>
      <Map type={type}></Map>
      </div>
    </>
  );
}

export default GetDst;
