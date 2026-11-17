// 문제2 정답: 방명록을 최신 글(번호가 큰 것)부터 보여 주고, 글 수 표시하기
const API = "";

async function load() {
  const response = await fetch(`${API}/api/messages`);
  const messages = await response.json();

  // reverse(): 배열 순서를 거꾸로 (나중에 쓴 글이 배열 뒤에 있으니까)
  messages.reverse();

  document.querySelector("#count").textContent = `글 ${messages.length}개 · 최신 글부터`;
  const list = document.querySelector("#list");
  for (const m of messages) {
    const li = document.createElement("li");
    li.textContent = `${m.id}. ${m.name}: ${m.text}`;
    list.append(li);
  }
}

load();
