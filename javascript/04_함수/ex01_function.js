// ex01_function.js : 자주 하는 일을 이름 붙여 묶어 두는 함수

// function 이름(매개변수) { 할 일; return 돌려줄 값; }
function add(a, b) {
  return a + b;                  // return: 결과를 돌려주고 함수를 끝내요
}

const result = add(3, 5);        // 함수 부르기(호출): 3 → a, 5 → b
console.log(result);             // 8
console.log(add(10, 20));        // 30

// return 없이 일만 하는 함수도 있어요
function greet(name) {
  console.log(`${name}님, 반가워요!`);
}
greet("민지");
greet("준호");
