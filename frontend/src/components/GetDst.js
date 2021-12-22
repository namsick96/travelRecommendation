import React from "react";
import Map from "./Map";

function GetDst() {
  const type = "DST";
  return (
    <>
      <h1>도착지를 선택하세요</h1>
      <Map type={type}></Map>
    </>
  );
}

export default GetDst;
