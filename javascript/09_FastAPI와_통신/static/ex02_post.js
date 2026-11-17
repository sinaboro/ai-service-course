// ex02_post.js : 폼에 쓴 내용을 JSON 으로 만들어 POST 로 보내기

const API = "";
const form = document.querySelector("#msg-form");
const status = document.querySelector("#status");
const result = document.querySelector("#result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();                          // 7장: 페이지 이동 막기

  // ① 보낼 데이터를 객체로 만들기 (키 이름은 서버 MessageIn 과 똑같이)
  const body = {
    name: document.querySelector("#name").value.trim(),
    text: document.querySelector("#text").value.trim(),
  };

  // ② fetch 의 두 번째 값(옵션)에 방법 · 머리말 · 본문을 적어요
  const response = await fetch(`${API}/api/messages`, {
    method: "POST",                                // 보내는 방법
    headers: { "Content-Type": "application/json" },  // "본문은 JSON 이에요"
    body: JSON.stringify(body),                    // 객체 → JSON 글자 (5장)
  });

  // ③ 응답 확인: 201 이면 성공, 422 면 규칙(글자 수)을 어긴 것
  const data = await response.json();
  result.textContent = JSON.stringify(data, null, 2);
  if (response.ok) {
    status.textContent = `${data.id}번 글로 등록했어요 (상태 코드 ${response.status})`;
    status.className = "ok";
    form.reset();                                  // 입력칸 비우기
  } else {
    status.textContent = `등록하지 못했어요 (상태 코드 ${response.status})`;
    status.className = "error";
  }
});
