# 버스 요금 계산 (여러 조건 응용)
age = 16
fee = 1500

if age >= 65 or age <= 6:
    fee = 0
elif 13 <= age <= 18:
    fee = int(fee * 0.8)       # 청소년 20% 할인
elif 7 <= age <= 12:
    fee = int(fee * 0.5)       # 어린이 50% 할인

print(f"{age}세 요금: {fee}원")

# in 으로 조건 검사하기
day = "토"
if day in ["토", "일"]:
    print(day, "요일은 주말 요금이 적용돼요.")
