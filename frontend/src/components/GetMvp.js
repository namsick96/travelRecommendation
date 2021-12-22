/* eslint-disable */
import React, { useState } from "react";
import Select from "react-select";
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";

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
      <div className="selection">
        <Select
          options={list}
          placeholder="장소를 입력해주세요"
          value={list.find((obj) => obj.value === key)}
          onChange={handleChange}
        />
        <button
          onClick={() => {
            dispatch({ type: "ADD_MVP", key: key });
          }}
        >
          <Link to="/dst">입력하기</Link>
        </button>
      </div>
    </>
  );
}
export default GetMvp;
