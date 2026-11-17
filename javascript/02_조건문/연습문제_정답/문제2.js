// 문제2 정답: 키 120cm 이상이고 나이 7살 이상이면 탈 수 있어요
const height = 125;
const age = 6;

if (height >= 120 && age >= 7) {
  console.log("탈 수 있어요!");
} else if (height < 120) {
  console.log("키가 120cm 이상이어야 해요");
} else {
  console.log("7살 이상만 탈 수 있어요");
}
