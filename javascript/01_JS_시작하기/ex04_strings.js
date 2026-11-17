// ex04_strings.js : 글자(문자열) 다루기

const city = "서울";
const temp = 23;

// 템플릿 문자열: 백틱(`)으로 감싸고 ${ } 안에 변수를 넣어요 (파이썬의 f-string)
console.log(`${city}의 기온은 ${temp}도예요`);

// + 로 이어 붙일 수도 있지만, 템플릿 문자열이 더 읽기 쉬워요
console.log(city + "의 기온은 " + temp + "도예요");

const msg = "  Hello JavaScript  ";
console.log(msg.length);          // 글자 수 (앞뒤 빈칸 포함): 20
console.log(msg.trim());          // 앞뒤 빈칸 없애기
console.log(msg.toUpperCase());   // 모두 대문자로
console.log(msg.includes("Java")); // "Java" 가 들어 있나? true
