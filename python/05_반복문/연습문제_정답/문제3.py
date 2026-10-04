# 문제 3. while을 이용해 2를 계속 곱해서 1000을 처음으로 넘는 값과 곱한 횟수를 출력하세요.

value = 1
count = 0
while value <= 1000:
    value *= 2
    count += 1
print(f"2를 {count}번 곱하면 {value}")
