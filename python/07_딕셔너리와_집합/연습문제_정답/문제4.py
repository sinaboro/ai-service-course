# 문제 4. scores = {"kim": 85, "lee": 92, "park": 78}에서 점수가 가장 높은 사람의 이름과 점수를 출력하세요.

scores = {"kim": 85, "lee": 92, "park": 78}
best = max(scores, key=scores.get)
print(f"1등: {best} ({scores[best]}점)")
