# 문제 1. data/students.csv를 읽어 수학 점수가 80점 이상인 학생의 이름과 수학 점수를 점수 높은 순으로 출력하세요.

import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

df = pd.read_csv("data/students.csv")
high = df[df["수학"] >= 80].sort_values("수학", ascending=False)
print(high[["이름", "수학"]])
