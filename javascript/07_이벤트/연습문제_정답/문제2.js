// 문제2 정답: ex04_todo.js 에 "완료한 일 모두 지우기" 버튼 더하기
let todos = [
  { id: 1, title: "JS 7장 읽기", done: true },
  { id: 2, title: "연습문제 풀기", done: false },
];
let nextId = 3;

const list = document.querySelector("#todo-list");
const left = document.querySelector("#left");
const input = document.querySelector("#todo-input");

function render() {
  list.textContent = "";
  for (const todo of todos) {
    const li = document.createElement("li");
    const check = document.createElement("input");
    check.type = "checkbox";
    check.checked = todo.done;
    check.addEventListener("change", () => {
      todo.done = !todo.done;
      render();
    });
    const span = document.createElement("span");
    span.textContent = todo.title;
    if (todo.done) span.className = "done";
    li.append(check, span);
    list.append(li);
  }
  left.textContent = `남은 할 일: ${todos.filter((t) => !t.done).length}개`;
}

document.querySelector("#todo-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const title = input.value.trim();
  if (title === "") return;
  todos.push({ id: nextId++, title: title, done: false });
  input.value = "";
  render();
});

// ⭐ 새로 더한 부분: 완료하지 않은 것만 남기기
document.querySelector("#clear").addEventListener("click", () => {
  todos = todos.filter((t) => !t.done);
  render();
});

render();
