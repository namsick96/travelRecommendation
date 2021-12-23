/*global kakao*/
/* eslint-disable */
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import "../css/Map.css"

function Map(props) {
  let dispatch = useDispatch();
  let [place, setPlace] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const script = document.createElement("script");
    script.async = true; // 브라우저가 페이지를 파싱되는 동안에도 스크립트가 실행됨.
    script.src =
      "https://dapi.kakao.com/v2/maps/sdk.js?appkey=c43d04a8684ca0542bf596c5c2000960&autoload=false";
    document.head.appendChild(script);
    script.onload = () => {
      kakao.maps.load(() => {
        let container = document.getElementById("map");
        let options = {
          center: new kakao.maps.LatLng(33.366589, 126.542296),
          level: 10,
        };
        let map = new kakao.maps.Map(container, options);
        // 마커가 표시될 위치입니다
        let markerPosition = new kakao.maps.LatLng(
          33.366589, 126.542296
        );

        // 마커를 생성합니다
        // 지도를 클릭한 위치에 표출할 마커입니다
        let marker = new kakao.maps.Marker({
          // 지도 중심좌표에 마커를 생성합니다
          position: map.getCenter(),
        });

        marker.setMap(map);
        // 기존의 함수 형태로 하면 this.state에서 this.state가 undefined이기 때문에 Arrow function을 이용해 상위 context의 객체를 this로 받아올 수 있도록 하여 현재 state 값을 변경
        kakao.maps.event.addListener(map, "click", (mouseEvent) => {
          // 클릭한 위도, 경도 정보를 가져옵니다
          var latlng = mouseEvent.latLng;

          // 마커 위치를 클릭한 위치로 옮깁니다
          marker.setPosition(latlng);

          // 클릭한 위치의 위도와 경도를 state의 x와 y에 setState해주기
          setPlace({
            ...place,
            x: latlng.getLat(), // this.state.x를 마커 위치의 위도로 값을 변경
            y: latlng.getLng(), // this.state.y를 마커 위치의 경도로 값을 변경
          });
        });
      });
    };
  }, []);

  return (
    <>
      <div id="map" style={{ width: "870px", height: "430px" , borderRadius:'20px', left:"43vh"}}></div>
      <button className="button4"
        onClick={() => {
          dispatch({ type: `ADD_${props.type}`, lat: place.x, lng: place.y });
        }}
      >
        {props.type === "SRC" ? <Link to="/mvp" style={{ textDecoration: 'none' , color: '#F4A644'}} >입력하기</Link> : null}
        {props.type === "DST" ? <Link to="/result"  style={{ textDecoration: 'none' , color: '#F4A644'}}>결과 확인</Link> : null}
      </button>
    </>
  );
}
export default Map;
