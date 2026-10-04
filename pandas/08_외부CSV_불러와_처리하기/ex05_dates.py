from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

df = pd.read_csv(DATA / "sales_excel_cp949.csv", encoding="cp949", thousands=",")
df["판매일"] = pd.to_datetime(df["판매일"], format="%Y.%m.%d")   # "2026.09.01" → 날짜
df["매출"] = df["수량"] * df["단가"]
print(df.dtypes)

df["요일"] = df["판매일"].dt.day_name()
df["주차"] = df["판매일"].dt.isocalendar().week

print(df.head(3))
print(df.groupby("주차")["매출"].sum())
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(df.groupby("요일")["매출"].sum().reindex(weekday_order))
print(df[df["판매일"].between("2026-09-10", "2026-09-12")])
