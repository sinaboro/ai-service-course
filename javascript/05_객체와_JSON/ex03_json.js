// ex03_json.js : 서버와 데이터를 주고받는 글자 형식, JSON

const memo = { title: "장보기", tags: ["우유", "빵"], important: true };

// 객체 → JSON 글자 (서버로 보낼 때)
const text = JSON.stringify(memo);
console.log(text);
console.log(typeof text);                 // string

// JSON 글자 → 객체 (서버에서 받았을 때)
const received = '{"id": 7, "title": "숙제하기", "done": false}';
const obj = JSON.parse(received);
console.log(obj.title);                   // 객체가 되었으니 점(.)으로 꺼낼 수 있어요
console.log(typeof obj);                  // object

// JSON 규칙: 키는 반드시 "큰따옴표", 마지막 쉼표 금지, 함수는 담을 수 없어요
