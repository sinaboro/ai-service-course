// app.js : 할 일 앱의 화면 동작 — 서버(FastAPI)와 fetch 로 대화해요
// 구성: ① 서버 요청 함수  ② 화면 그리기  ③ 기능(목록 · 추가 · 완료 · 삭제)  ④ 이벤트 연결

const API = "/api/todos";

const form = document.querySelector("#todo-form");
const input = document.querySelector("#todo-input");
const list = document.querySelector("#todo-list");
const statusEl = document.querySelector("#status");
const summary = document.querySelector("#summary");

// ---------- ① 서버 요청 함수 ----------
// fetch 를 부르고, 실패하면 오류를 던지고, 성공하면 JSON 을 돌려줘요
// 9장에서 매번 쓰던 코드를 함수 하나로 묶은 거예요
async function request(url, options = {}) {
  const response = await fetch(url, options);
  const data = await response.json();
  if (!response.ok) {
    // FastAPI 가 보낸 오류 문구(detail)가 글자면 그걸 쓰고, 아니면 상태 코드를 보여 줘요
    const message = typeof data.detail === "string" ? data.detail : `요청 실패 (${response.status})`;
    throw new Error(message);
  }
  return data;
}

// JSON 본문을 보내는 요청의 옵션을 만들어 주는 함수 (POST, PATCH 에서 써요)
function jsonOptions(method, body) {
  return {
    method: method,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  };
}

function showStatus(text, kind = "") {
  statusEl.textContent = text;
  statusEl.className = kind;
}

// ---------- ② 화면 그리기 ----------
function render(todos) {
  list.textContent = "";
  for (const todo of todos) {
    const li = document.createElement("li");
    if (todo.done) li.className = "done";

    const check = document.createElement("input");
    check.type = "checkbox";
    check.checked = todo.done;
    check.setAttribute("aria-label", `${todo.title} 완료`);
    check.addEventListener("change", () => toggleTodo(todo.id, check.checked));

    const title = document.createElement("span");
    title.textContent = todo.title;           // textContent: 글자로만 넣어서 안전해요

    const del = document.createElement("button");
    del.className = "delete";
    del.textContent = "삭제";
    del.addEventListener("click", () => deleteTodo(todo.id));

    li.append(check, title, del);
    list.append(li);
  }
  const left = todos.filter((t) => !t.done).length;
  summary.textContent = `남은 할 일 ${left}개 / 전체 ${todos.length}개`;
}

// ---------- ③ 기능 ----------
// 목록 불러오기 (GET)
async function loadTodos() {
  try {
    const todos = await request(API);
    render(todos);
  } catch (error) {
    showStatus("서버에 연결할 수 없어요. uvicorn 으로 서버를 켰는지 확인하세요.", "error");
  }
}

// 추가 (POST)
async function addTodo(title) {
  try {
    await request(API, jsonOptions("POST", { title: title }));
    await loadTodos();
    showStatus(`"${title}" 를 추가했어요`, "ok");
  } catch (error) {
    showStatus(`추가하지 못했어요: ${error.message}`, "error");
  }
}

// 완료 표시 바꾸기 (PATCH)
async function toggleTodo(id, done) {
  try {
    await request(`${API}/${id}`, jsonOptions("PATCH", { done: done }));
    await loadTodos();
    showStatus(done ? "완료로 표시했어요" : "완료를 취소했어요", "ok");
  } catch (error) {
    showStatus(`바꾸지 못했어요: ${error.message}`, "error");
  }
}

// 삭제 (DELETE)
async function deleteTodo(id) {
  try {
    await request(`${API}/${id}`, { method: "DELETE" });
    await loadTodos();
    showStatus("삭제했어요", "ok");
  } catch (error) {
    showStatus(`삭제하지 못했어요: ${error.message}`, "error");
  }
}

// ---------- ④ 이벤트 연결 ----------
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const title = input.value.trim();
  if (title === "") {
    showStatus("할 일을 입력해 주세요", "error");
    return;
  }
  input.value = "";
  addTodo(title);
});

loadTodos();       // 페이지를 열면 바로 목록 불러오기
