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

# 문제: 공부 시간(x)으로 점수(y) 예측하기
# x: 공부 시간(문제), y: 점수(정답) — 데이터 8개
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([52, 55, 61, 64, 70, 73, 78, 83])

# ① 프로그래밍: 사람이 규칙을 직접 정함
def rule(hours):
    return 50 + 4 * hours            # "한 시간에 4점씩 오르겠지?" (짐작)

# ② 머신러닝: 데이터를 보고 규칙(기울기 w, 절편 b)을 컴퓨터가 찾음
# polyfit(x, y, 1): 점들에 가장 잘 맞는 직선(1차식)의 기울기 w 와 절편 b 를 찾아 줘요
w, b = np.polyfit(x, y, deg=1)
print(f"사람이 정한 규칙   : 점수 = 50 + 4.00 × 시간")
print(f"데이터로 배운 규칙 : 점수 = {b:.2f} + {w:.2f} × 시간")
print("9시간 공부하면?  사람:", rule(9), " 머신러닝:", round(b + w * 9, 1))

# 그래프: 검은 점 = 실제 데이터, 회색 점선 = 사람 규칙, 빨간 선 = 배운 규칙
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(x, y, label="실제 데이터", color="black")
ax.plot(x, rule(x), "--", label="사람이 정한 규칙", color="gray")
ax.plot(x, b + w * x, label="데이터로 배운 규칙", color="crimson")
ax.set_xlabel("공부 시간")
ax.set_ylabel("점수")
ax.legend()
# 그림 파일로 저장 (images 폴더)
fig.savefig(IMG / "ex01_rule_vs_learning.png", dpi=100, bbox_inches="tight")
