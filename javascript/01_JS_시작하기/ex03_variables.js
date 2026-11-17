// ex03_variables.js : 값을 담는 상자, 변수

// const: 한 번 넣으면 바꿀 수 없는 상자 (기본으로 이것을 써요)
const name = "김철수";
console.log(name);

// let: 나중에 값을 바꿀 수 있는 상자
let score = 80;
console.log("처음 점수:", score);
score = 95;                      // let 은 다시 넣을 수 있어요
console.log("바뀐 점수:", score);

// name = "이영희";  ← const 에 다시 넣으면 오류(TypeError)가 나요

// typeof: 값의 종류(자료형)를 알려 줘요
console.log(typeof name);        // string  (문자열)
console.log(typeof score);       // number  (숫자)
console.log(typeof true);        // boolean (참/거짓)

// 값을 아직 넣지 않은 변수는 undefined (정해지지 않음)
let memo;
console.log(memo);
