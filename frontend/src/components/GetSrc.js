import React from "react";
import Map from "./Map";
import "../css/Map.css";

function GetSrc() {
  const type = "SRC";
  return (
    <>
      <h3 className="bar1">여기올레</h3>
      <div className="container1">
      <h1 className="sug">당신의 출발지를 선택해주세요</h1>
      <Map className="map" type={type}></Map>
      
      </div>
    </>
  );
}

export default GetSrc;
