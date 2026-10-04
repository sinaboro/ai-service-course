# 중첩 반복문: 구구단 2 ~ 4 단
for dan in range(2, 5):
    print(f"--- {dan}단 ---")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")

# 별 삼각형
for line in range(1, 6):
    print("*" * line)
