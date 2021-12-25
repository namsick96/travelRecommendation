/* eslint-disable */

export default [
  {
    id: 0,
    question: "유형 테스트 시작",
  },
  {
    id: 1,
    question: "음식이 나왔을 때 나는?",
    answer: [
      "사진부터 찍는다.",
      "먹다가 사진 찍을 걸 하고 후회한다.",
      "다 먹고 잘 먹은 식당 사진을 찍는다.",
      "사진 찍을 시간이 어딨어, 바로 흡입한다.",
    ],
    result: [
      {activity : 0, inside : 0, nature : 0, photo : 1, cafe : 0},
      {activity : 0, inside : 0.6, nature : 0, photo : 0, cafe : 1},
      {activity : 0, inside : 0, nature : 0, photo : 0.3, cafe : 0},
      {activity : 0, inside : 0, nature : 0, photo : 0, cafe : 0},
    ],
  },
  {
    id: 2,
    question:
      "한라산에 간다면 당신은?",
    answer: [
      "한라산 백록담과 함께 인생샷 남기기 ",
      "한라산은 사진으로만 ^^ 애초에 안 올라간다.",
      "등산 도중 쉴 때마다 사진찍기",
      "한라산 입구에서 사진만 찍고 다른 사진 스팟 돌기 ",
    ],
    result: [
      {activity : 0.9, inside : 0, nature : 0.9, photo :0.7 , cafe : 0},
      {activity : 0, inside : 1, nature : 0, photo : 0, cafe : 0},
      {activity : 0.7, inside : 0, nature : 0.9, photo : 1, cafe : 0},
      {activity : 0.2, inside : 0.3, nature : 0, photo : 1, cafe : 0},
    ],
  },
  {
    id: 3,
    question: "아래 예시 중 가장 방문하고 싶은 제주도 관광지는?",
    answer: [
      "선물도 사고 녹차도 마실 수 있는 오설록 박물관",
      "노을을 볼 수 있는 성산일출봉",
      "유명 작가들의 작품을 전시한 빛의 벙커",
      "용두암 해안도로 카페거리",
    ],
    result: [
      {activity : 0.3, inside : 0.4, nature : 0.7, photo : 0.7, cafe : 0.6},
      {activity : 0.8, inside : 0, nature : 0.9, photo : 0.6, cafe : 0},
      {activity : 0, inside : 1, nature : 0, photo : 1, cafe : 0},
      {activity : 0, inside : 0.5, nature : 0.6, photo : 1, cafe : 1},
    ],
  },
  {
    id: 4,
    question: "내가 제주 바다에 간다면?",
    answer: [
      "일단 뛰어든다",
      "바닷가가 보이는 오션뷰 카페에서 바라본다",
      "바닷가를 산책한다",
      "바닷가 사진을 찍는다",
    ],
    result: [
      {activity : 1, inside : 0, nature : 0.9, photo : 0, cafe : 0},
      {activity : 0.1, inside : 0.8, nature : 0.6, photo : 1, cafe : 1},
      {activity : 0.1, inside : 0.8, nature : 0.6, photo : 1, cafe : 1},
       {activity : 0.5, inside : 0.5, nature : 0.8, photo : 1, cafe : 0},
    ],
  },
  {
    id: 5,
    question: "제주도에 간다면 어떤 숙소가 좋을까?",
    answer: [
      "다른 사람들을 만날 수 있는 게스트 하우스",
      "프라이빗하고 여유롭게 즐길 수 있는 호텔",
      "인스타에서 핫한 감성펜션",
      "한라산 중턱에 고즈넉하게 위치한 민박집",
    ],
    result: [
      {activity : 1, inside : 0.5, nature : 0, photo : 0, cafe : 0},
      {activity : 0, inside : 1, nature : 0, photo : 0, cafe : 0},
      {activity : 0, inside : 0.5, nature : 0, photo : 1, cafe : 0},
      {activity : 0, inside : 0.5, nature : 1, photo : 0, cafe : 0},
    ],
  },
  {
    id: 6,
    question: "늦은 제주의 밤, 가장 하고 싶은 것은?",
    answer: [
      "호텔 방 안에서 커피 한 잔",
      "제주 해안도로 야간 드라이브",
      "제주 밤바다 산책",
      "선술집에서 술 한 잔",
    ],
    result: [
      {activity : 0, inside : 1, nature : 0, photo : 0, cafe : 0.7},
      {activity : 0.7, inside : 0, nature : 0.7, photo : 0, cafe : 0},
      {activity : 0.6, inside : 0, nature : 1, photo : 0, cafe : 0},
      {activity : 0, inside : 0.7, nature : 0, photo : 0, cafe : 0},
    ],
  },
  {
    id: 7,
    question: "다음 중 제주도에 한 가지를 꼭 가져가야 한다면?",
    answer: [
      "운동화",
      "남는 건 사진 뿐! 카메라",
      "당충전을 위한 간식상자",
      "읽을 책",
    ],
    result: [
      {activity : 1, inside : 0, nature : 1, photo : 0, cafe : 0},
      {activity : 0, inside : 0, nature : 0, photo : 1, cafe : 0},
      {activity : 0, inside : 0, nature : 0, photo : 0, cafe : 1},
      {activity : 0, inside : 1, nature : 0, photo : 0, cafe : 0},
    ],
  },
  {
    id: 8,
    question: "혼자 제주도에 간다면 꼭 해보고 싶은 것은?",
    answer: [
      "수상 액티비티 체험",
      "전시, 미술관, 박물관 도장깨기",
      "아무도 없는 숲길 걷기",
      "제주 맛집 방문",
    ],
    result: [
      {activity : 1, inside : 0, nature : 0.9, photo : 0, cafe : 0},
      {activity : 0, inside : 1, nature : 0, photo : 0.7, cafe : 0},
      {activity : 1, inside : 0, nature : 1, photo : 0, cafe : 0},
      {activity : 0, inside : 0.5, nature : 0, photo : 0.5, cafe : 0},
    ],
  },
  {
    id: 9,
    question: "제주도에 도착해서 가장 먼저 할 행동은?",
    answer: [
      "공항에 있는 돌하르방이랑 사진찍기",
      "짐 던져놓고 관광지 돌아다니기",
      "힘드니까 호텔 가서 쉬기",
      "4면이 다른 색깔인 제주바다 보러가기",
    ],
    result: [
      {activity : 0, inside : 0, nature : 0, photo : 1, cafe : 0},
      {activity : 1, inside : 0, nature : 0.5, photo : 0, cafe : 0},
      {activity : 0, inside : 1, nature : 0, photo : 0, cafe : 0},
      {activity : 0.4, inside : 0, nature : 1, photo : 0.5, cafe : 0},
    ],
  },
  {
    id: 10,
    question: "나의 산책 스팟은?",
    answer: [
      "제주도 올레길",
      "여미지 식물원",
      "용두암 해안도로 카페거리",
      "산책 안할꼬얌",
    ],
    result: [
      {activity : 1, inside : 0, nature : 1, photo : 0, cafe : 0},
      {activity : 0, inside : 0, nature : 1, photo : 0.3, cafe : 0},
      {activity : 0, inside : 0, nature : 0, photo : 0.8, cafe : 1},
      {activity : 0, inside : 1, nature : 0, photo : 0, cafe : 0},
    ],
  },
];
