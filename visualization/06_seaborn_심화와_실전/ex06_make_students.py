# 실습용 학생 생활 데이터 만들기 (data/students_life.csv)
from pathlib import Path
import numpy as np
import pandas as pd

# 학생 200명의 학년 · 동아리를 무작위로 (p: 동아리별 뽑힐 확률)
rng = np.random.default_rng(seed=2026)
n = 200
grade = rng.choice(["1학년", "2학년", "3학년"], n)
study = rng.uniform(0, 6, n).round(1)                       # 하루 공부 시간
# 수면 · 휴대폰 시간도 공부 시간과 관련 있게 만들기 (+ 잡음)
sleep = (8.5 - study * 0.35 + rng.normal(0, 0.6, n)).round(1)
phone = (5 - study * 0.5 + rng.normal(0, 1, n)).clip(0.5).round(1)
club = rng.choice(["운동", "음악", "코딩", "없음"], n, p=[0.3, 0.2, 0.2, 0.3])
score = (50 + study * 7 - phone * 2 + rng.normal(0, 6, n)).clip(0, 100).round()

# 열 이름을 붙여 표로 만들고 data 폴더에 저장
df = pd.DataFrame({"grade": grade, "club": club, "study_h": study,
                   "sleep_h": sleep, "phone_h": phone, "score": score})
out = Path(__file__).parent / "data" / "students_life.csv"
df.to_csv(out, index=False, encoding="utf-8")
print(df.head())
print(df.shape, "→", out.name)
