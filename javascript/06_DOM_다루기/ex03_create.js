// ex03_create.js : 배열의 데이터로 목록(li)을 새로 만들어 화면에 붙이기

const todos = ["우유 사기", "JS 6장 공부", "운동 30분"];
const list = document.querySelector("#todo-list");

for (const text of todos) {
  const li = document.createElement("li");   // ① 새 태그 만들기 (아직 화면에는 없어요)
  li.textContent = text;                     // ② 글자 넣기
  list.append(li);                           // ③ ul 안에 붙이기 → 이제 화면에 보여요
}

document.querySelector("#count").textContent = `모두 ${todos.length}개`;
