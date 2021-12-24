/* eslint-disable */

import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getResult } from "../reducers/place";
import "../css/loading.css";
import loading from "../css/loading.png";
import marker from "../css/maker.png";
import font from "../font/font.css";


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
       <h3 className="bar" style={{fontFamily : 'WandohopeR'}}>여기올레</h3>
      {loading === true ? <Loading></Loading> : null}
      {showResult === true ? (
        <ResultComponent data={state.place.result.result}></ResultComponent>
      ) : null}
    </>
  );
}

function Loading() {
  return( 
      <div className="testcont">
      <div className="cont">
      <div className="load"  style={{fontFamily: 'EliceDigitalBaeum_Bold'}}>#로딩 중</div>
       <img className="loading2" src={loading}></img>
      </div></div>
    
    );
}

function ResultComponent(props) {
  console.log("props");
  console.log(props.data);
  const { places, restaurant, alchol } = props.data;
  console.log(places);
  console.log(restaurant);
  console.log(alchol);

  
  return (
    <div>
      <div>여기올레?  <span>가 추천하는 여행 코스</span></div>
      <img className="marker1" src={marker}></img><img className="marker3"  src={marker}></img>
      <hr className="vector"></hr>
      <div>  <span className="sp">출발지</span>
      {
        places.map((place,i)=> {
          return <span className="course" key={i}><img className="marker2"  src={marker}></img> {place}</span>
        })
      }
      <span className="dt">도착지</span>
      </div>
      <div >
      {
        restaurant.map((place, i)=> {
          return <span key={i} className="restaurant">{place}</span>
        })
      }
      </div>
      <div>
      {      
        alchol.map((place, i)=> {
          return <span key={i}  className="alchol">{place}</span>
        })
      }
      </div>
      
    </div>
  );
}

export default Result;
