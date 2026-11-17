// 문제2 정답: 섭씨 → 화씨 바꾸기 (화씨 = 섭씨 × 9 / 5 + 32)
const input = "25";                    // 입력칸에서 받은 값이라고 생각해요 (문자열)
const celsius = Number(input);         // 숫자로 바꾸기
const fahrenheit = celsius * 9 / 5 + 32;

console.log(`섭씨 ${celsius}도는 화씨 ${fahrenheit.toFixed(1)}도예요`);
