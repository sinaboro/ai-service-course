// 문제1 정답: 버튼을 누르면 data/quotes.json 을 불러와 무작위 명언 하나 보여 주기
const status = document.querySelector("#status");
const quote = document.querySelector("#quote");

document.querySelector("#btn").addEventListener("click", async () => {
  status.textContent = "불러오는 중...";
  try {
    const response = await fetch("../data/quotes.json");
    if (!response.ok) throw new Error(`응답 오류 (${response.status})`);
    const quotes = await response.json();
    // Math.random(): 0 이상 1 미만의 무작위 수 → 배열 번호로 바꾸기
    const pick = quotes[Math.floor(Math.random() * quotes.length)];
    quote.textContent = `"${pick.text}" — ${pick.who}`;
    quote.classList.remove("hidden");
    status.textContent = "";
  } catch (error) {
    status.textContent = `불러오지 못했어요: ${error.message}`;
    status.className = "error";
  }
});
