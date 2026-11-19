// ex03_guestbook.js : 목록(GET) · 쓰기(POST) · 삭제(DELETE) + 로딩 · 오류 처리 한 번에

const API = "";
const form = document.querySelector("#msg-form");
const status = document.querySelector("#status");
const list = document.querySelector("#list");

// 상태 문구를 보여 주는 작은 함수 (kind: "ok" 초록, "error" 빨강, "" 기본)
function showStatus(text, kind = "") {
  status.textContent = text;
  status.className = kind;
}

// ① 목록 그리기: 글마다 [삭제] 버튼을 달아요
function render(messages) {
  list.textContent = "";
  for (const m of messages) {
    const li = document.createElement("li");
    const name = document.createElement("strong");
    name.className = "msg-name";
    name.textContent = m.name;
    const text = document.createElement("span");
    text.textContent = m.text;
    const del = document.createElement("button");
    del.className = "ghost";
    del.textContent = "삭제";
    del.addEventListener("click", () => removeMessage(m.id));
    li.append(name, text, del);
    list.append(li);
  }
}

// ② GET: 목록 불러오기
async function loadMessages() {
  showStatus("불러오는 중...");
  try {
    const response = await fetch(`${API}/api/messages`);
    if (!response.ok) throw new Error(`응답 오류 ${response.status}`);
    const messages = await response.json();
    render(messages);
    showStatus(`글 ${messages.length}개`);
  } catch (error) {
    // 서버가 꺼져 있으면 fetch 자체가 실패해요 (TypeError: Failed to fetch)
    showStatus("서버에 연결할 수 없어요. 서버(uvicorn)가 켜져 있나요?", "error");
  }
}

// ③ POST: 글 쓰기
async function addMessage(name, text) {
  try {
    const response = await fetch(`${API}/api/messages`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: name, text: text }),  // 객체 → JSON 글자로 바꿔 보내기
    });
    if (response.status === 422) {
      showStatus("이름은 1 ~ 10자, 남길 말은 1 ~ 100자로 써 주세요", "error");
      return;
    }
    if (!response.ok) throw new Error(`응답 오류 ${response.status}`);
    form.reset();
    await loadMessages();                       // 서버의 최신 목록으로 다시 그리기
    showStatus("등록했어요", "ok");
  } catch (error) {
    showStatus(`등록하지 못했어요: ${error.message}`, "error");
  }
}

// ④ DELETE: 글 지우기 (주소에 글 번호를 넣어요)
async function removeMessage(id) {
  try {
    const response = await fetch(`${API}/api/messages/${id}`, { method: "DELETE" });
    if (!response.ok) {
      const data = await response.json();      // {"detail": "그 글을 찾을 수 없어요"}
      throw new Error(data.detail);
    }
    await loadMessages();
    showStatus(`${id}번 글을 지웠어요`, "ok");
  } catch (error) {
    showStatus(`지우지 못했어요: ${error.message}`, "error");
  }
}

// ⑤ 이벤트 연결과 시작
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const name = document.querySelector("#name").value.trim();
  const text = document.querySelector("#text").value.trim();
  if (name === "" || text === "") {             // 서버에 보내기 전에 먼저 검사 (2장)
    showStatus("이름과 남길 말을 모두 써 주세요", "error");
    return;
  }
  addMessage(name, text);
});

loadMessages();                                 // 페이지를 열자마자 목록 불러오기
