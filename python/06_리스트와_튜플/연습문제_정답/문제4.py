# 문제 4. scores = [55, 92, 78, 61, 88]에서 60점 미만인 점수의 개수를 구하세요.

scores = [55, 92, 78, 61, 88]
fail = len([s for s in scores if s < 60])
print("불합격 인원:", fail)
