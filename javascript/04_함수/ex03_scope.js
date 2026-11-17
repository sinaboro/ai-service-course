// ex03_scope.js : 변수는 자기가 만들어진 { } 안에서만 쓸 수 있어요

const appName = "할 일 앱";        // 함수 밖: 어디서나 쓸 수 있어요

function showTitle() {
  const count = 3;                // 함수 안: 이 함수 안에서만 쓸 수 있어요
  console.log(`${appName} - 할 일 ${count}개`);
}
showTitle();

// console.log(count);  ← 오류! count 는 함수 밖에서 보이지 않아요 (ReferenceError)

if (true) {
  let inside = "if 안의 변수";
  console.log(inside);
}
// console.log(inside); ← 오류! { } 밖에서는 보이지 않아요
console.log("함수 밖에서는 appName 만 쓸 수 있어요:", appName);
