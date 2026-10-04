# 문제 2. 연도 year = 2024가 윤년인지 판별하세요. (4의 배수이면서 100의 배수가 아니거나, 400의 배수면 윤년)

year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 평년입니다.")
