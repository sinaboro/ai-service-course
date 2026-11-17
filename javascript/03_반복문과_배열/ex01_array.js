// ex01_array.js : 여러 값을 순서대로 담는 배열

const fruits = ["사과", "바나나", "포도"];
console.log(fruits);

// 번호(인덱스)는 0 부터 시작해요
console.log(fruits[0]);              // 사과
console.log(fruits[2]);              // 포도
console.log(fruits.length);          // 개수: 3

// 맨 뒤에 추가: push, 맨 뒤를 꺼내기: pop
fruits.push("딸기");
console.log(fruits);
const last = fruits.pop();
console.log(`꺼낸 것: ${last}`, fruits);

// 값 바꾸기
fruits[1] = "망고";
console.log(fruits);
