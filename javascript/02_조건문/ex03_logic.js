// ex03_logic.js : 조건 여러 개를 합치기

const id = "admin";
const password = "1234";

// && (그리고): 둘 다 참이어야 참
if (id === "admin" && password === "1234") {
  console.log("로그인 성공");
}

// || (또는): 둘 중 하나만 참이어도 참
const day = "토";
if (day === "토" || day === "일") {
  console.log("주말이에요");
}

// ! (아니다): 참 ↔ 거짓을 뒤집어요
const isLoggedIn = false;
if (!isLoggedIn) {
  console.log("먼저 로그인해 주세요");
}
