# 리스트와 반복문
scores = [90, 75, 88, 62, 95]

total = 0
for s in scores:
    total += s
print("합계:", total)
print("평균:", total / len(scores))

# 내장 함수로 한 번에
print("sum:", sum(scores), "max:", max(scores), "min:", min(scores))

# 80점 이상만 모으기
high = []
for s in scores:
    if s >= 80:
        high.append(s)
print("80점 이상:", high)

# 번호와 함께
for i, s in enumerate(scores, start=1):
    print(f"{i}번 학생: {s}점")
