# break: 반복 멈추기 / continue: 이번만 건너뛰기
for i in range(1, 11):
    if i == 6:
        break           # 6 이 되면 반복 종료
    print(i, end=" ")
print()

for i in range(1, 11):
    if i % 3 == 0:
        continue        # 3 의 배수는 건너뛰기
    print(i, end=" ")
print()
