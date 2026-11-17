// ex01_click.js : 버튼을 누르면(클릭 이벤트) 숫자가 바뀌어요

let count = 0;
const num = document.querySelector("#num");

// 화면에 숫자를 다시 그리는 함수
function render() {
  num.textContent = count;
}

// addEventListener("이벤트 이름", 함수): "이 일이 생기면 이 함수를 불러 줘" (4장 콜백)
document.querySelector("#plus").addEventListener("click", () => {
  count++;
  render();
});

document.querySelector("#minus").addEventListener("click", () => {
  count--;
  render();
});

document.querySelector("#reset").addEventListener("click", () => {
  count = 0;
  render();
});
