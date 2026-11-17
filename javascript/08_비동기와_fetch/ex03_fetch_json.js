// ex03_fetch_json.js : fetch 로 JSON 파일을 가져와 화면에 그리기
// ⚠️ 파일을 더블클릭(file://)해서 열면 fetch 가 막혀요. Live Server 로 열어요

async function loadMembers() {
  // ① fetch(주소): 서버(여기서는 Live Server)에 파일을 달라고 요청 → 응답이 올 때까지 기다리기
  const response = await fetch("data/members.json");

  // ② 응답 본문(JSON 글자)을 객체로 바꾸기 (5장 JSON.parse 를 대신 해 줘요)
  const members = await response.json();
  console.log(members);

  // ③ 6장처럼 화면에 그리기
  const list = document.querySelector("#members");
  for (const m of members) {
    const li = document.createElement("li");
    li.textContent = `${m.name} — ${m.role}`;
    list.append(li);
  }
}

loadMembers();
