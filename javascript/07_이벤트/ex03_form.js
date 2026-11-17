// ex03_form.js : 폼을 제출할 때(submit 이벤트) 페이지 이동을 막고, 입력값으로 목록 만들기

const form = document.querySelector("#add-form");
const input = document.querySelector("#item");
const list = document.querySelector("#list");
const message = document.querySelector("#message");

form.addEventListener("submit", (event) => {
  // ⭐ 폼은 제출하면 페이지가 새로고침돼요. 그걸 막아요
  event.preventDefault();

  const text = input.value.trim();
  if (text === "") {                        // 2장 빈 값 검사
    message.textContent = "살 것을 입력해 주세요";
    message.className = "error";
    return;                                 // 함수를 여기서 끝내요
  }

  const li = document.createElement("li"); // 6장 태그 만들기
  li.textContent = text;
  list.append(li);

  message.textContent = `"${text}" 를 추가했어요`;
  message.className = "ok";
  input.value = "";                         // 입력칸 비우기
  input.focus();                            // 다시 입력하기 편하게 커서 두기
});
