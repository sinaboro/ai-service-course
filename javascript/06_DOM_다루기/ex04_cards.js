// ex04_cards.js : 객체 배열(5장)을 카드 모양으로 화면에 그리기
// 9 ~ 10장에서는 이 데이터를 서버에서 받아와요

const courses = [
  { title: "HTML · CSS", level: "입문", hours: 46 },
  { title: "JavaScript", level: "입문", hours: 40 },
  { title: "FastAPI", level: "초급", hours: 12 },
];

const box = document.querySelector("#cards");

// 카드 하나를 만드는 함수 (4장 함수)
function makeCard(course) {
  const article = document.createElement("article");
  article.className = "card";

  const h2 = document.createElement("h2");
  h2.textContent = course.title;

  const p = document.createElement("p");
  p.textContent = `${course.level} · ${course.hours}시간`;

  article.append(h2, p);                     // 여러 개를 한 번에 붙일 수 있어요
  return article;
}

for (const c of courses) {
  box.append(makeCard(c));
}
