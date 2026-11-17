// 문제2 정답: 서버에서 받은 JSON 글자를 객체로 바꿔 평균 점수 구하기
const text = '[{"name": "민지", "score": 90}, {"name": "준호", "score": 75}, {"name": "지수", "score": 83}]';

const students = JSON.parse(text);        // 글자 → 객체 배열
let sum = 0;
for (const s of students) {
  sum += s.score;
}
console.log(`평균: ${(sum / students.length).toFixed(1)}점`);
