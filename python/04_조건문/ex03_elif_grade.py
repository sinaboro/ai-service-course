# if - elif - else: 여러 경우 중 처음으로 참인 것 하나만 실행
score = 85

# 90 이상이면 여기서 끝, 아니면 다음 조건으로
if score >= 90:
    grade = "A"
# 위 조건이 거짓이고 80 이상일 때 (= 80 ~ 89)
elif score >= 80:
    grade = "B"
# 70 ~ 79
elif score >= 70:
    grade = "C"
# 위 조건이 모두 거짓일 때
else:
    grade = "F"

print(f"{score}점은 {grade}학점입니다.")
