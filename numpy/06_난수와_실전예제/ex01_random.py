import numpy as np

rng = np.random.default_rng(seed=42)    # 난수 생성기 (seed 가 같으면 결과도 같음)

print(rng.integers(1, 7, size=5))        # 1 ~ 6 정수 5개 (7은 미포함)
print(rng.random(3).round(3))            # 0 ~ 1 실수 3개
print(rng.integers(0, 100, size=(2, 3))) # 2행 3열 정수
print(rng.normal(170, 5, size=4).round(1))   # 평균 170, 표준편차 5 인 정규분포
print(rng.choice(["가위", "바위", "보"], size=3))

cards = np.arange(1, 6)
rng.shuffle(cards)                       # 순서 섞기 (원본이 바뀜)
print(cards)
