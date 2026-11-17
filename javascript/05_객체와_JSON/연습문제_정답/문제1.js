// 문제1 정답: 가격이 20000원 이상인 책의 제목만 출력하기
const books = [
  { title: "자바스크립트 첫걸음", price: 18000 },
  { title: "웹 개발 교과서", price: 32000 },
  { title: "파이썬 입문", price: 22000 },
];

const expensive = books.filter((b) => b.price >= 20000);
for (const b of expensive) {
  console.log(b.title);
}
