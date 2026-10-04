import numpy as np

rng = np.random.default_rng(seed=7)

# 주사위 6000 번 던지기
dice = rng.integers(1, 7, size=6000)
values, counts = np.unique(dice, return_counts=True)
for v, c in zip(values, counts):
    print(f"{v}: {c}번 ({c / dice.size:.1%})")
print("평균 눈:", dice.mean().round(2))

# 로또: 1 ~ 45 중 중복 없이 6개
lotto = rng.choice(np.arange(1, 46), size=6, replace=False)
print("로또 번호:", np.sort(lotto))
