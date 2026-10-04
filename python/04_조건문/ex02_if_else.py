# if - else: 참이면 위, 거짓이면 아래
num = 7

# % 는 나머지: 2로 나눈 나머지가 0 이면 짝수
if num % 2 == 0:
    print(num, "은(는) 짝수")
# if 조건이 거짓일 때 실행
else:
    print(num, "은(는) 홀수")

# 조건부 표현식: 값 하나를 고를 때 한 줄로
result = "짝수" if num % 2 == 0 else "홀수"
print("한 줄로:", result)
