// 문제1 정답: 버튼을 누를 때마다 답을 보였다 숨기고, 버튼 글자도 바꾸기
const btn = document.querySelector("#toggle-btn");
const answer = document.querySelector("#answer");

btn.addEventListener("click", () => {
  answer.classList.toggle("hidden");                 // 있으면 떼고 없으면 붙이기
  const hidden = answer.classList.contains("hidden");
  btn.textContent = hidden ? "답 보기" : "답 숨기기";
});
