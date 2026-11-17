// ex02_input.js : 입력할 때마다(input 이벤트) 글자 수를 보여 주기

const MAX = 30;
const intro = document.querySelector("#intro");
const counter = document.querySelector("#counter");

intro.addEventListener("input", () => {
  const len = intro.value.length;          // 입력칸의 글자는 .value 로 읽어요
  counter.textContent = `${len} / ${MAX}`;

  // 30자를 넘으면 빨간 글씨 (6장 classList)
  if (len > MAX) {
    counter.classList.add("error");
  } else {
    counter.classList.remove("error");
  }
});
