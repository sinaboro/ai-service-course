// ex02_if.js : 조건에 따라 다른 일을 하기

const score = 85;
let grade;

// 위에서부터 차례로 검사하고, 처음으로 참인 곳 하나만 실행해요
if (score >= 90) {
  grade = "A";
} else if (score >= 80) {
  grade = "B";
} else if (score >= 70) {
  grade = "C";
} else {
  grade = "F";            // 위 조건이 모두 거짓일 때
}
console.log(`${score}점은 ${grade}학점이에요`);

// 조건이 하나뿐이면 if 만 써도 돼요
if (score >= 60) {
  console.log("합격이에요!");
}
