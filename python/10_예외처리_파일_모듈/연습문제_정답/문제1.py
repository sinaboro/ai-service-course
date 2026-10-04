# 문제 1. 리스트 data = ["10", "abc", "30", "4.5", "20"]에서 정수로 바꿀 수 있는 값만 더하세요. 바꿀 수 없으면 "건너뜀: 값"을 출력하세요.

data = ["10", "abc", "30", "4.5", "20"]
total = 0
for d in data:
    try:
        total += int(d)
    except ValueError:
        print("건너뜀:", d)
print("합계:", total)
