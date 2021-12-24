import React from "react";
import Map from "./Map";
import "../css/Map.css";
import font from "../font/font.css";

function GetDst() {
  const type = "DST";
  return (
    <>
      <h3 className="bar1" style={{fontFamily : 'WandohopeR'}}>여기올레</h3>
      <div className="container1">
      <h1 className="sug" style={{fontFamily: 'EliceDigitalBaeum_Bold'}}>당신의 도착지를 선택해주세요</h1>
      <Map type={type}></Map>
      </div>
    </>
  );
}

export default GetDst;
