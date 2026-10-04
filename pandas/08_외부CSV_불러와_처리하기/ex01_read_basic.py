from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

print("데이터 폴더:", DATA.name, "/ 파일 있음?", (DATA / "students.csv").exists())

df = pd.read_csv(DATA / "students.csv")
print(df.head(3))
print(df.shape)
print(df.dtypes)

df["총점"] = df[["국어", "영어", "수학"]].sum(axis=1)
df["평균"] = df[["국어", "영어", "수학"]].mean(axis=1).round(1)
print(df.sort_values("총점", ascending=False).head(3))
print(df.groupby("반")["평균"].mean().round(1))
