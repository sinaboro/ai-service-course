// ex02_arrow.js : 함수를 짧게 쓰는 화살표 함수 (=>)

// 보통 함수
function square1(x) {
  return x * x;
}

// 화살표 함수: const 이름 = (매개변수) => { ... }
const square2 = (x) => {
  return x * x;
};

// 한 줄로 바로 돌려줄 때는 { } 와 return 을 생략할 수 있어요
const square3 = (x) => x * x;

console.log(square1(4), square2(4), square3(4));   // 16 16 16

// 매개변수 기본값: 값을 안 넣으면 기본값을 써요
const hello = (name = "손님") => `안녕하세요, ${name}님`;
console.log(hello("지수"));
console.log(hello());
