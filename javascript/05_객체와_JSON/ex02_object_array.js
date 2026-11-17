// ex02_object_array.js : 객체 여러 개를 배열에 담기 (서버에서 받는 데이터가 거의 이 모양이에요)

const todos = [
  { id: 1, title: "우유 사기", done: true },
  { id: 2, title: "JS 공부하기", done: false },
  { id: 3, title: "운동하기", done: false },
];

// 하나씩 꺼내 쓰기
for (const todo of todos) {
  const mark = todo.done ? "✔" : " ";     // 조건 ? 참일 때 : 거짓일 때
  console.log(`[${mark}] ${todo.id}. ${todo.title}`);
}

// 아직 안 한 일만 고르기 (4장 filter)
const left = todos.filter((t) => !t.done);
console.log(`남은 할 일: ${left.length}개`);

// id 로 하나 찾기 (4장 find)
const found = todos.find((t) => t.id === 2);
console.log(found.title);

// 제목만 모아 새 배열 (4장 map)
console.log(todos.map((t) => t.title));
