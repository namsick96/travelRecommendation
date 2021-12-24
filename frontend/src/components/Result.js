/* eslint-disable */

import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getResult } from "../reducers/place";

function Result() {
  let [loading, setLoading] = useState(true);
  let [showResult, setShowResult] = useState(false);
  let state = useSelector((state) => state);

  let dispatch = useDispatch();

  useEffect(() => {
    getResult(state.place).then((result) => {
      dispatch(result);
      setLoading(false);
      setShowResult(true);
    });
  }, []);

  return (
    <>
      <p>최종 결과 페이지</p>
      {loading === true ? <Loading></Loading> : null}
      {showResult === true ? (
        <ResultComponent data={state.place.result.result}></ResultComponent>
      ) : null}
    </>
  );
}

function Loading() {
  return <div>로딩 중</div>;
}

function ResultComponent(props) {
  console.log("props");
  console.log(props.data);
  const { places, restaurant, alchol } = props.data;
  console.log(places);
  console.log(restaurant);
  console.log(alchol);

  
  [...places].unshift('출발지');
  [...places].push('도착지');
  
  return (
    <div>
      <p>test</p>
      <div className="course">
      {
        places.map((place,i)=> {
          return <div key={i}>{place}</div>
        })
      }
      </div>
      <div className="restaurant">
      {
        restaurant.map((place, i)=> {
          return <div key={i}>{place}</div>
        })
      }
      </div>
      <div className="alchol">
      {      
        alchol.map((place, i)=> {
          return <div key={i}>{place}</div>
        })
      }
      </div>
      
    </div>
  );
}

export default Result;
