# 문제 4. name = "김철수", price = 45000, count = 3일 때 f-string으로 "김철수님, 총 135,000원입니다."를 출력하세요.

name = "김철수"
price = 45000
count = 3
print(f"{name}님, 총 {price * count:,}원입니다.")
