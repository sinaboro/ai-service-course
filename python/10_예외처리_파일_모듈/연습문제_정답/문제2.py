# 문제 2. 1부터 5까지의 제곱을 한 줄에 하나씩 squares.txt에 저장한 뒤, 다시 읽어서 합계를 출력하세요.

with open("squares.txt", "w", encoding="utf-8") as f:
    for i in range(1, 6):
        f.write(f"{i ** 2}\n")

total = 0
with open("squares.txt", "r", encoding="utf-8") as f:
    for line in f:
        total += int(line.strip())
print("제곱의 합:", total)
