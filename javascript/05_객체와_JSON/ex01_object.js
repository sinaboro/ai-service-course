// ex01_object.js : 이름표(키)와 값을 짝지어 담는 객체

const user = {
  name: "김민지",       // 키: 값
  age: 21,
  isStudent: true,
};
console.log(user);

// 값 꺼내기: 점(.) 표기
console.log(user.name);
console.log(`${user.name}님은 ${user.age}살이에요`);

// 값 바꾸기 · 새 키 추가하기
user.age = 22;
user.email = "minji@example.com";
console.log(user);

// 키 이름이 변수에 들어 있을 때는 대괄호 [ ] 를 써요
const key = "email";
console.log(user[key]);
