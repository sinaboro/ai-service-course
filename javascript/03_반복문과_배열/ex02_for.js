// ex02_for.js : 같은 일을 여러 번 반복하기

// for (시작; 계속할 조건; 한 번 끝날 때마다) { 반복할 일 }
for (let i = 1; i <= 3; i++) {       // i++ 는 i = i + 1 과 같아요
  console.log(`${i}번째 반복`);
}

const foods = ["김밥", "라면", "떡볶이"];

// 배열의 번호(i)가 필요할 때
for (let i = 0; i < foods.length; i++) {
  console.log(i, foods[i]);
}

// ⭐ for...of: 배열의 값을 하나씩 꺼내요 (번호가 필요 없을 때 가장 편해요)
for (const food of foods) {
  console.log(`오늘 메뉴: ${food}`);
}
