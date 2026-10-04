import numpy as np

rng = np.random.default_rng(seed=2026)
names = np.array([f"학생{i}" for i in range(1, 11)])
subjects = np.array(["국어", "영어", "수학"])
scores = rng.integers(40, 101, size=(10, 3))      # 10명 x 3과목

print("점수표 (앞 3명):")
print(scores[:3])

total = scores.sum(axis=1)
avg = scores.mean(axis=1)
print("\n과목별 평균:", scores.mean(axis=0).round(1))
print("과목별 최고:", scores.max(axis=0))

best = avg.argmax()
print(f"\n전체 1등: {names[best]} (평균 {avg[best]:.1f})")

rank = np.argsort(total)[::-1]
print("상위 3명:", names[rank[:3]])

passed = np.all(scores >= 60, axis=1)            # 모든 과목 60 이상
print("\n전 과목 통과:", names[passed])
print("통과율:", f"{passed.mean():.0%}")

grade = np.where(avg >= 90, "A", np.where(avg >= 80, "B", np.where(avg >= 70, "C", "F")))
for n, a, g in zip(names[:5], avg[:5], grade[:5]):
    print(f"{n}: {a:.1f} → {g}")
