// ex04_todo.js : 데이터(배열) → 화면 그리기 → 이벤트로 데이터 바꾸고 다시 그리기
// 이 흐름이 10장 미니 프로젝트의 뼈대예요

let todos = [
  { id: 1, title: "JS 7장 읽기", done: false },
  { id: 2, title: "연습문제 풀기", done: false },
];
let nextId = 3;

const form = document.querySelector("#todo-form");
const input = document.querySelector("#todo-input");
const list = document.querySelector("#todo-list");
const left = document.querySelector("#left");

// ① 데이터를 보고 화면 전체를 다시 그리는 함수
function render() {
  list.textContent = "";                     // 목록 비우기
  for (const todo of todos) {
    const li = document.createElement("li");

    const check = document.createElement("input");
    check.type = "checkbox";
    check.checked = todo.done;
    check.addEventListener("change", () => toggle(todo.id));   // 완료 표시

    const span = document.createElement("span");
    span.textContent = todo.title;
    if (todo.done) span.className = "done";

    const del = document.createElement("button");
    del.textContent = "삭제";
    del.className = "ghost";
    del.addEventListener("click", () => remove(todo.id));     // 삭제

    li.append(check, span, del);
    list.append(li);
  }
  const count = todos.filter((t) => !t.done).length;
  left.textContent = `남은 할 일: ${count}개`;
}

// ② 데이터를 바꾸는 함수들 — 바꾼 뒤에는 항상 render()
function add(title) {
  todos.push({ id: nextId, title: title, done: false });
  nextId++;
  render();
}

function toggle(id) {
  const todo = todos.find((t) => t.id === id);
  todo.done = !todo.done;                    // 참 ↔ 거짓 뒤집기
  render();
}

function remove(id) {
  todos = todos.filter((t) => t.id !== id);  // 그 id 만 빼고 남기기
  render();
}

// ③ 이벤트 연결
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const title = input.value.trim();
  if (title === "") return;
  add(title);
  input.value = "";
});

render();                                    // 처음 화면 그리기
