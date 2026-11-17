// ex04_empty_check.js : 입력값이 비었는지 검사하기 (폼에서 자주 써요)

function check(text) {
  // trim() 으로 앞뒤 빈칸을 지운 뒤, 길이가 0 이면 빈 입력이에요
  if (text.trim() === "") {
    console.log(`"${text}" → 내용을 입력해 주세요`);
  } else if (text.length > 10) {
    console.log(`"${text}" → 10글자 이하로 써 주세요`);
  } else {
    console.log(`"${text}" → 좋아요!`);
  }
}

check("");              // 빈 문자열
check("   ");           // 빈칸만 있는 문자열
check("우유 사기");
check("아주아주 긴 할 일 제목입니다");
