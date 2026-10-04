import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np

# 검증 사진 전체에서 "bottle" 탐지 결과를 모은 것: (신뢰도, 정답과 IoU ≥ 0.5 인가?)
dets = [(0.95, True), (0.91, True), (0.88, False), (0.84, True), (0.80, True), (0.71, False),
        (0.66, True), (0.52, False), (0.45, True), (0.33, False), (0.21, False)]
n_truth = 7                                     # 검증 사진 속 실제 병 개수

dets.sort(reverse=True)                         # 신뢰도 높은 순서
# TP 누적 합 · FP 누적 합: 기준을 한 단계씩 낮출 때마다 맞은 수 · 틀린 수가 쌓여요
tp = np.cumsum([1 if ok else 0 for _, ok in dets])
fp = np.cumsum([0 if ok else 1 for _, ok in dets])
precision = tp / (tp + fp)
recall = tp / n_truth
# 기준별로 정밀도 · 재현율 출력
for (conf, ok), p, r in zip(dets, precision, recall):
    print(f"기준 {conf:.2f} 까지 인정 → {'맞음' if ok else '틀림'} | 정밀도 {p:.2f} 재현율 {r:.2f}")

# AP = 정밀도-재현율 곡선 아래 넓이 (뒤쪽 최댓값으로 곡선을 평평하게 만든 뒤)
p_env = np.maximum.accumulate(precision[::-1])[::-1]
r_all = np.concatenate([[0], recall])
ap = float(np.sum((r_all[1:] - r_all[:-1]) * p_env))
print(f"AP50 (bottle) = {ap:.3f}")

# AP 를 넓이로 보여 주는 그래프
fig, ax = plt.subplots(figsize=(5.5, 4))
ax.plot(recall, precision, "o-", label="정밀도-재현율")
ax.step(recall, p_env, where="pre", color="crimson", label="AP 계산용 곡선")
ax.fill_between(recall, p_env, step="pre", alpha=0.15, color="crimson")
ax.set_xlabel("재현율 (놓치지 않기)"); ax.set_ylabel("정밀도 (헛것 말하지 않기)")
ax.set_xlim(0, 1.05); ax.set_ylim(0, 1.05); ax.legend(); ax.set_title(f"AP50 = {ap:.3f}")
fig.savefig(IMG / "ex03_map.png", dpi=100, bbox_inches="tight")
