import numpy as np

# 난수 생성기 (seed 고정 → 실행할 때마다 같은 결과)
rng = np.random.default_rng(seed=7)

# 주사위 6000 번 던지기
# integers(1, 7): 1 이상 7 미만 정수 = 주사위 눈 1 ~ 6
dice = rng.integers(1, 7, size=6000)
# 눈마다 나온 횟수 세기
values, counts = np.unique(dice, return_counts=True)
# 횟수와 비율 출력 (6000번이면 눈마다 약 1/6 = 16.7%)
for v, c in zip(values, counts):
    print(f"{v}: {c}번 ({c / dice.size:.1%})")
print("평균 눈:", dice.mean().round(2))

# 로또: 1 ~ 45 중 중복 없이 6개
# choice(..., replace=False): 한 번 뽑은 번호는 다시 안 뽑기
lotto = rng.choice(np.arange(1, 46), size=6, replace=False)
print("로또 번호:", np.sort(lotto))
