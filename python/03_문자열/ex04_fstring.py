# f-string: 문자열 안에 변수 넣기
name = "홍길동"
age = 20
score = 87.6543

print(f"이름: {name}, 나이: {age}")
print(f"내년 나이: {age + 1}")            # 계산도 가능
print(f"점수: {score:.2f}")               # 소수점 2자리
print(f"가격: {1234567:,}원")              # 천 단위 콤마
print(f"[{name:>6}]")                     # 6칸 오른쪽 정렬
print(f"[{'abc':<6}]")                    # 6칸 왼쪽 정렬
