// ex01_compare.js : 두 값을 비교하면 결과는 true(참) 또는 false(거짓)

console.log(10 > 5);      // true
console.log(10 <= 5);     // false

// ⭐ 같은지 비교는 === (등호 3개), 다른지 비교는 !==
console.log(5 === 5);     // true
console.log(5 !== 3);     // true

// ⚠️ == (등호 2개)는 자료형이 달라도 몰래 바꿔서 비교해요 → 헷갈리니 쓰지 않아요
console.log(5 == "5");    // true  (숫자 5 와 문자열 "5" 를 같다고 봄)
console.log(5 === "5");   // false (자료형까지 비교 → 이게 정확해요)
