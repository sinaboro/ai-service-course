// ex02_class.js : CSS class 를 붙이고 떼어서 모양 바꾸기
// 모양(CSS)은 style.css 에 미리 만들어 두고, JS 는 class 만 바꿔요

const notice = document.querySelector("#notice");
notice.classList.add("highlight");        // class 붙이기 → 노란 상자

const secret = document.querySelector("#secret");
secret.classList.remove("hidden");        // class 떼기 → 보이게

const status = document.querySelector("#status");
status.textContent = "저장했어요";
status.classList.add("ok");               // 초록 글씨

// toggle: 있으면 떼고, 없으면 붙여요 (7장에서 버튼과 함께 써요)
console.log(notice.classList.contains("highlight"));   // true

// style 로 직접 바꿀 수도 있지만, class 를 쓰는 편이 관리하기 쉬워요
status.style.fontWeight = "bold";
