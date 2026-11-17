// 문제1 정답: 키(cm)와 몸무게(kg)를 받아 BMI 를 돌려주는 함수
// BMI = 몸무게 / (키(m) × 키(m))
function bmi(heightCm, weightKg) {
  const h = heightCm / 100;        // cm → m
  return weightKg / (h * h);
}

const value = bmi(170, 65);
console.log(`BMI: ${value.toFixed(1)}`);
