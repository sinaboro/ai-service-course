// ex01_select.js : HTML 태그를 찾아(querySelector) 글자를 바꾸기

// document.querySelector("CSS 선택자"): 조건에 맞는 첫 번째 태그 하나를 찾아요
const title = document.querySelector("#title");    // id 는 #
console.log(title.textContent);                    // 지금 글자: 원래 제목

// textContent 에 값을 넣으면 화면의 글자가 바뀌어요
title.textContent = "JavaScript 가 바꾼 제목";

// querySelectorAll: 맞는 태그를 모두 찾아요 (for...of 로 하나씩)
const msgs = document.querySelectorAll(".msg");    // class 는 .
let n = 1;
for (const p of msgs) {
  p.textContent = `${n}번째 문단을 JS 가 바꿨어요`;
  n++;
}
console.log(`문단 ${msgs.length}개를 바꿨어요`);
