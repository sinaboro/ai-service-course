// ex05_numbers.js : 숫자 계산과 문자열 → 숫자 바꾸기

console.log(7 + 3, 7 - 3, 7 * 3, 7 / 2); // 10 4 21 3.5
console.log(7 % 3);                      // 나머지: 1

// ⚠️ 문자열 + 숫자 는 계산이 아니라 "이어 붙이기" 가 돼요
console.log("3" + 1);                    // "31"

// 입력칸의 값은 항상 문자열이에요. Number() 로 숫자로 바꿔서 계산해요
const input = "3";
console.log(Number(input) + 1);          // 4

// 숫자로 바꿀 수 없으면 NaN (Not a Number, 숫자가 아님)
console.log(Number("abc"));              // NaN

// 소수점 자리 맞추기: toFixed(자릿수) → 결과는 문자열
const avg = 85.6666;
console.log(avg.toFixed(1));             // "85.7"
