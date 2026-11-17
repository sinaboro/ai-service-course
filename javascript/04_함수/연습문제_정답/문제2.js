// 문제2 정답: map 으로 모든 가격을 10% 할인하고, filter 로 5000원 이하만 고르기
const prices = [3000, 6000, 5500, 12000];

const sale = prices.map((p) => Math.round(p * 0.9));   // Math.round: 반올림
console.log(sale);                          // [2700, 5400, 4950, 10800]

const under5000 = sale.filter((p) => p <= 5000);
console.log(under5000);                     // [2700, 4950]
