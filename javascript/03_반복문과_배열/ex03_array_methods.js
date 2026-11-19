// ex03_array_methods.js : 배열에서 찾기 · 합치기 · 자르기

const colors = ["빨강", "주황", "노랑", "초록"];

console.log(colors.includes("노랑"));   // 들어 있나? true
console.log(colors.indexOf("초록"));    // 몇 번째? 3 (없으면 -1)
console.log(colors.join(" / "));        // 하나의 문자열로 합치기
console.log(colors.slice(1, 3));        // 1번부터 3번 앞까지 잘라 새 배열로

// 숫자 배열 정렬: (a, b) => a - b 를 넣으면 작은 수부터 (4장에서 자세히)
const nums = [30, 5, 100, 12];
nums.sort((a, b) => a - b);           // (a, b) => a - b : 숫자 작은 순 정렬 규칙
console.log(nums);
