// ex04_score_stats.js : 반복문으로 합계 · 평균 · 최고점 구하기

const scores = [72, 95, 88, 64, 91];

let sum = 0;                  // 합계를 모을 변수 (0 부터 시작)
let max = scores[0];          // 최고점 후보: 일단 첫 번째 점수

for (const s of scores) {
  sum = sum + s;              // 하나씩 더하기 (sum += s 라고 써도 돼요)
  if (s > max) {
    max = s;                  // 더 큰 점수를 만나면 바꾸기
  }
}

const avg = sum / scores.length;
console.log(`합계: ${sum}`);
console.log(`평균: ${avg.toFixed(1)}`);
console.log(`최고점: ${max}`);
