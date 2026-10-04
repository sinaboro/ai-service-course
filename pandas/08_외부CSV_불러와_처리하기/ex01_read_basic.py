from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

# 파일이 정말 있는지 먼저 확인 (경로 실수가 가장 흔한 오류)
print("데이터 폴더:", DATA.name, "/ 파일 있음?", (DATA / "students.csv").exists())

# CSV 읽기 → 앞 3행, (행 수, 열 수), 열마다 자료형 확인
df = pd.read_csv(DATA / "students.csv")
print(df.head(3))
print(df.shape)
print(df.dtypes)

# 세 과목 열을 골라 가로(axis=1)로 합계 · 평균 → 새 열 만들기
df["총점"] = df[["국어", "영어", "수학"]].sum(axis=1)
df["평균"] = df[["국어", "영어", "수학"]].mean(axis=1).round(1)
# 총점 상위 3명 / 반별 평균
print(df.sort_values("총점", ascending=False).head(3))
print(df.groupby("반")["평균"].mean().round(1))
