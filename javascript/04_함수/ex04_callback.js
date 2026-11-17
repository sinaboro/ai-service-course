// ex04_callback.js : 함수를 다른 함수에 넘겨 "나중에 불러 줘" 하고 맡기기 (콜백)
// 7장 이벤트, 8장 비동기에서 계속 쓰는 아주 중요한 생각이에요

const prices = [1000, 2500, 4000];

// forEach: 배열의 값마다 넘겨준 함수를 한 번씩 불러 줘요
prices.forEach((p) => {
  console.log(`가격: ${p}원`);
});

// map: 값마다 함수를 불러 "바뀐 값" 으로 새 배열을 만들어요
// (Math.round: 반올림. 소수 계산의 아주 작은 오차를 없애요)
const withTax = prices.map((p) => Math.round(p * 1.1));
console.log(withTax);

// filter: 함수가 true 를 돌려준 값만 모아 새 배열을 만들어요
const cheap = prices.filter((p) => p < 3000);
console.log(cheap);

// find: 조건에 맞는 첫 번째 값 하나를 찾아요 (없으면 undefined)
console.log(prices.find((p) => p > 2000));
