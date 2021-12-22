import React from "react";
import Map from "./Map";

function GetSrc() {
  const type = "SRC";
  return (
    <>
      <h1>출발지를 선택하세요</h1>
      <Map type={type}></Map>
    </>
  );
}

export default GetSrc;
