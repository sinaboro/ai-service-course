// 문제1 정답: 1초마다 GET /api/hello 를 불러 서버 시각을 화면에 보여 주기
const API = "";
const timeEl = document.querySelector("#time");
const status = document.querySelector("#status");

async function tick() {
  try {
    const response = await fetch(`${API}/api/hello`);
    const data = await response.json();
    timeEl.textContent = data.time;
    status.textContent = "";
  } catch (error) {
    status.textContent = "서버에 연결할 수 없어요";
    status.className = "error";
  }
}

tick();                         // 처음 한 번 바로
setInterval(tick, 1000);        // setInterval: 정해진 시간마다 계속 불러요 (8장 setTimeout 의 반복판)
