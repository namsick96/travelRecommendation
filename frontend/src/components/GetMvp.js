/* eslint-disable */
import React, { useState } from "react";
import Select from "react-select";
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import '../css/Mvp.css';
import font from "../font/font.css";
import "../css/Mvp.css";
import placeList from '../data/placeList.json';

const data = placeList;
const obj = Object.values(data);

const list = [
];

function GetMvp() {
  console.log(data);
  // console.log(obj);

  data.map((place, i) => {
    const temp = {label: place, value:i}
    console.log(temp);
    list.push(temp);
  })

  let dispatch = useDispatch();
  let [key, setKey] = useState(0);

  const handleChange = (e) => {
    console.log(e.value);
    setKey(e.value);
  };

  return (
    <>
      <h4 className="bar" style={{fontFamily : 'WandohopeR'}}>여기 올레</h4>
      <h3 className="rec" style={{fontFamily: 'EliceDigitalBaeum_Bold'}}>꼭 방문하고 싶은 PLACE를 골라주세요</h3>
      <div className="selection1">
        <Select
          options={list}
          placeholder="장소를 입력해주세요"
          value={list.find((obj) => obj.value === key)}
          onChange={handleChange}
        />
        <button
          className="button1"
          onClick={() => {
            dispatch({ type: "ADD_MVP", key: key });
          }}
        >
          <Link to="/dst" style={{ textDecoration: "none", color: "white" ,fontFamily: 'Cafe24SsurroundAir'}}>
            선택완료
          </Link>
        </button>
      </div>
    </>
  );
}
export default GetMvp;
