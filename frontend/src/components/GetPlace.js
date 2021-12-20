/* eslint-disable */
import React, { useState } from "react";
import Select from "react-select";

const list = [
  // label, value 형식은 지켜야 함
  { label: "Option1", value: "Shark" },
  { label: "Option2", value: "Dolphin" },
  { label: "Option3", value: "Whale" },
  { label: "Option4", value: "Octopus" },
  { label: "Option5", value: "Crab" },
  { label: "Option6", value: "Lobster" },
];

function GetPlace() {
  return (
    <>
      <div className="selection">
        <div>
          <Select options={list} />
          <button>입력</button>
        </div>
      </div>
    </>
  );
}
export default GetPlace;
