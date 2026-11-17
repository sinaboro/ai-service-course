// ex04_loading_error.js : 기다리는 동안 "불러오는 중", 실패하면 오류 문구 보여 주기

const status = document.querySelector("#status");
const list = document.querySelector("#members");

async function load(url) {
  status.textContent = "불러오는 중...";          // ① 기다리는 동안 안내
  status.className = "";
  list.textContent = "";

  try {
    const response = await fetch(url);
    // ② 404(없음), 500(서버 오류)처럼 실패한 응답이면 직접 오류를 던져요
    if (!response.ok) {
      throw new Error(`서버 응답 오류 (${response.status})`);
    }
    const members = await response.json();
    for (const m of members) {
      const li = document.createElement("li");
      li.textContent = `${m.name} — ${m.role}`;
      list.append(li);
    }
    status.textContent = `${members.length}명을 불러왔어요`;
    status.className = "ok";
  } catch (error) {
    // ③ try 안에서 오류가 나면 여기로 와요 (인터넷 끊김, 위에서 던진 오류 등)
    status.textContent = `불러오지 못했어요: ${error.message}`;
    status.className = "error";
  }
}

document.querySelector("#ok-btn").addEventListener("click", () => load("data/members.json"));
document.querySelector("#bad-btn").addEventListener("click", () => load("data/nothing.json"));
