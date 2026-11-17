// 문제2 정답: 배열에서 짝수만 골라 새 배열 만들기
const nums = [3, 8, 15, 22, 7, 10];
const evens = [];                 // 빈 배열에서 시작

for (const n of nums) {
  if (n % 2 === 0) {
    evens.push(n);                // 짝수면 담기
  }
}
console.log(evens);               // [8, 22, 10]
