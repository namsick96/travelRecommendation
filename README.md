## 1. 팀원 소개

  팀원: 권대규, 안지훈, 오성민, 유동욱, 이가람, 이은지, 정현지

## 2. 프로젝트 기간

  - 2021.11-2021.12

## 3. 프로젝트 개요

  제주도 관광객 1500만명 시대! 제주도에서 당신에게 맞는 여행지를 추천해주는 여기올레 서비스입니다.

  당신의 여행 타입을 진단해주고 당신이 하루동안 가면 좋을 여행지를 효율적인 동선을 고려해 추천해 줍니다.

## 4. 프로젝트 사용 기술 스택

  - **Front-End**
    - Javascript ES6
    - React 17.0.2
    - React-Redux 7.2.6
    - Axios 0.24.0
    - CSS3
  - **Back-End**
    - Java 11
    - Spring boot 2.6.2
    - Python3.8
    - Flask 1.1.1
  - **Model**
    - python3.8
    - Selenium
  - **AWS**
    - AWS EC2
  - **External API**
    - Kakao Map API

## 5. 프로젝트 아키텍쳐

<img width="1752" alt="스크린샷 2022-01-03 오후 10 10 10" src="https://user-images.githubusercontent.com/61309514/147934320-97edaf1e-913f-4a5a-93d1-c84665e758db.png">

저희 프로젝트는 총 3개의 서버로 구성되어있습니다. 우선 react로 만들어진 프론트엔드 서버가 있습니다. 해당 서버에서 react를 활용해 페이지를 구성하였습니다. react로 만들어진 코드는 빌드되어 nginx 웹서버를 이용해 aws ec2환경에 배포하였습니다. 두번째로는 백엔드 서버입니다. 백엔드 서버는 Spring boot로 제작되었으며 내장 tomcat을 이용하였습니다. 이 또한 aws ec2에 배포되었습니다. 마지막으로 모델 서버는 flask를 이용해 백엔드 서버와 통신하며 사용자에게 추천할 데이터를 전달하였습니다. 또한 모델 서버는 Google maps에서 크롤링한 데이터와 사용자로부터 입력받은 데이터를 활용해 사용자에게 추천 식당, 까페, 여행지, 여행지 방문 순서를 계산하여 사용자에게 제공합니다. 이때 여행지 간의 거리는 Kakao maps API를 통해 받은 위치 정보를 바탕으로 계산합니다.


## 6. 프로젝트 상세 내용
  - [Design 위키 페이지 링크](https://github.com/namsick96/travelRecommendation/wiki/1.-Design)
  - [Front-End 위키 페이지](https://github.com/namsick96/travelRecommendation/wiki/2.-Front-End)
  - [Back-End 위키 페이지 링크](https://github.com/namsick96/travelRecommendation/wiki/3.-Back-End)
  - [Model 위키 페이지 링크](https://github.com/namsick96/travelRecommendation/wiki/4.-Recommendation-Model)
  - [Crawling 위키 페이지 링크](https://github.com/namsick96/travelRecommendation/wiki/5.-Crawling)

## 7. 프로젝트 결과물
<img width="1440" alt="스크린샷 2022-01-01 오후 2 30 46" src="https://user-images.githubusercontent.com/87167786/147844650-1f256126-8148-4473-aa22-1b662d60e3ba.png">
<img width="1440" alt="스크린샷 2022-01-01 오후 2 30 57" src="https://user-images.githubusercontent.com/87167786/147844662-b046cf0b-2959-4bb6-9e29-358338915ca7.png">
<img width="1440" alt="스크린샷 2022-01-01 오후 2 31 05" src="https://user-images.githubusercontent.com/87167786/147844665-3aad6c46-56db-4884-9dff-2df64c4d0de0.png">
<img width="1440" alt="스크린샷 2022-01-01 오후 2 43 33" src="https://user-images.githubusercontent.com/87167786/147844736-026c01cf-69fa-4fb0-913c-96e1a4b9419e.png">
<img width="1440" alt="스크린샷 2022-01-01 오후 2 31 27" src="https://user-images.githubusercontent.com/87167786/147844676-a8efde80-6fc3-4ce2-9381-e83bd37cfd24.png">

## 8. 프로젝트 발표 링크
  - [발표 영상 링크](https://www.youtube.com/watch?v=tHB20xRZgZA)
