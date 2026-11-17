// 문제1 정답: 팀원 배열로 카드 그리기 (이름은 h2, 역할은 p)
const team = [
  { name: "김민지", role: "화면 담당" },
  { name: "이준호", role: "서버 담당" },
  { name: "박지수", role: "AI 모델 담당" },
];

const box = document.querySelector("#team");
for (const m of team) {
  const card = document.createElement("article");
  card.className = "card";
  const h2 = document.createElement("h2");
  h2.textContent = m.name;
  const p = document.createElement("p");
  p.textContent = m.role;
  card.append(h2, p);
  box.append(card);
}
