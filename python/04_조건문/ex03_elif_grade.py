# if - elif - else: 여러 경우 중 처음으로 참인 것 하나만 실행
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"{score}점은 {grade}학점입니다.")
