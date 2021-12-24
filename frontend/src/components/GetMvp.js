/* eslint-disable */
import React, { useState } from "react";
import Select from "react-select";
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import '../css/Mvp.css';
import font from "../font/font.css";

const list = [
  // label, value 형식은 지켜야 함
  { label: "Option1", value: 0 },
  { label: "Option2", value: 1 },
  { label: "Option3", value: 2 },
  { label: "Option4", value: 3 },
  { label: "Option5", value: 4 },
  { label: "Option6", value: 5 },
];

function GetMvp() {
  let dispatch = useDispatch();
  let [key, setKey] = useState(0);

  const handleChange = (e) => {
    console.log(e.value);
    setKey(e.value);
  };

  return (
    <>
      <h4 className="bar" style={{fontFamily : 'WandohopeR'}}>여기 올레</h4>
      <h3 className="rec">꼭 방문하고 싶은 PLACE를 골라주세요</h3>
      <div className="selection1">
        <Select 
          options={list}
          placeholder="장소를 입력해주세요"
          value={list.find((obj) => obj.value === key)}
          onChange={handleChange}
        />
        <button className="button1"
          onClick={() => {
            dispatch({ type: "ADD_MVP", key: key });
          }}
        >
          <Link to="/dst"  style={{ textDecoration: 'none' , color: 'white'}}>선택완료</Link>
        </button>
      </div>
    </>
  );
}
export default GetMvp;
