// ex01_get.js : fetch 로 FastAPI 서버에 GET 요청을 보내고 JSON 결과 받기

// 서버 주소. 서버가 보내 준 페이지(http://127.0.0.1:8000)로 열었으면 빈 문자열이면 돼요
// Live Server(5500)로 열었다면 "http://127.0.0.1:8000" 으로 바꿔요 (CORS, 5절)
const API = "";

const result = document.querySelector("#result");
const list = document.querySelector("#list");

// ① GET /api/hello : 8장의 fetch 와 똑같아요. 주소만 서버 API 로 바뀌었어요
document.querySelector("#hello-btn").addEventListener("click", async () => {
  const response = await fetch(`${API}/api/hello`);
  const data = await response.json();          // {"message": "...", "time": "..."}
  result.textContent = `${data.message} (서버 시각 ${data.time})`;
});

// ② GET /api/messages : 객체 배열을 받아 목록으로 그리기 (6장)
document.querySelector("#list-btn").addEventListener("click", async () => {
  const response = await fetch(`${API}/api/messages`);
  const messages = await response.json();
  result.textContent = JSON.stringify(messages, null, 2);   // 받은 JSON 을 보기 좋게
  list.textContent = "";
  for (const m of messages) {
    const li = document.createElement("li");
    li.textContent = `${m.name}: ${m.text}`;
    list.append(li);
  }
});
