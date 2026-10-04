import numpy as np

rng = np.random.default_rng(seed=2026)
# 학생 이름 10개: 학생1 ~ 학생10
names = np.array([f"학생{i}" for i in range(1, 11)])
subjects = np.array(["국어", "영어", "수학"])
scores = rng.integers(40, 101, size=(10, 3))      # 10명 x 3과목

print("점수표 (앞 3명):")
print(scores[:3])

# 학생별 총점 · 평균 (axis=1: 가로 방향)
total = scores.sum(axis=1)
avg = scores.mean(axis=1)
# 과목별 평균 · 최고점 (axis=0: 세로 방향)
print("\n과목별 평균:", scores.mean(axis=0).round(1))
print("과목별 최고:", scores.max(axis=0))

# argmax: 가장 큰 값의 위치(번호) → 그 번호로 이름 꺼내기
best = avg.argmax()
print(f"\n전체 1등: {names[best]} (평균 {avg[best]:.1f})")

# argsort: 작은 순서의 위치 목록 → [::-1] 로 뒤집으면 큰 순서
rank = np.argsort(total)[::-1]
print("상위 3명:", names[rank[:3]])

passed = np.all(scores >= 60, axis=1)            # 모든 과목 60 이상
# passed 는 True/False 배열 → 이름 배열에 넣으면 True 인 학생만 / mean() = True 비율
print("\n전 과목 통과:", names[passed])
print("통과율:", f"{passed.mean():.0%}")

# np.where(조건, 참일 때, 거짓일 때) 를 겹쳐서 학점 매기기
grade = np.where(avg >= 90, "A", np.where(avg >= 80, "B", np.where(avg >= 70, "C", "F")))
# 앞의 5명만 평균과 학점 출력
for n, a, g in zip(names[:5], avg[:5], grade[:5]):
    print(f"{n}: {a:.1f} → {g}")
