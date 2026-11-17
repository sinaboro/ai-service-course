// ex02_await.js : await 로 "끝날 때까지 기다렸다가" 다음 줄 실행하기

// 정해진 시간 뒤에 끝나는 약속(Promise)을 돌려주는 함수
// (이 줄은 외우지 않아도 돼요. "기다리는 일" 을 흉내 내는 도구예요)
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

// await 는 async 가 붙은 함수 안에서만 쓸 수 있어요
async function cook() {
  console.log("라면 물 올리기");
  await wait(1000);                 // 1초 기다리기 (끝날 때까지 이 함수는 멈춰요)
  console.log("1초 뒤: 물이 끓었어요");
  await wait(500);
  console.log("0.5초 뒤: 라면 완성!");
  return "라면";
}

async function main() {
  const food = await cook();        // cook() 이 끝날 때까지 기다렸다가 결과 받기
  console.log(`먹기: ${food}`);
}

main();
console.log("cook 을 기다리는 동안에도 이 줄이 먼저 실행돼요");
