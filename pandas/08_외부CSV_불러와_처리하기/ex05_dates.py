from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

# thousands=",": "4,000" 같은 글자를 숫자 4000 으로 읽기
df = pd.read_csv(DATA / "sales_excel_cp949.csv", encoding="cp949", thousands=",")
df["판매일"] = pd.to_datetime(df["판매일"], format="%Y.%m.%d")   # "2026.09.01" → 날짜
df["매출"] = df["수량"] * df["단가"]
print(df.dtypes)

# 날짜 열의 .dt 로 요일 이름 · 주차(몇 번째 주) 꺼내기
df["요일"] = df["판매일"].dt.day_name()
df["주차"] = df["판매일"].dt.isocalendar().week

print(df.head(3))
print(df.groupby("주차")["매출"].sum())
# 요일은 가나다순이 아니라 월 ~ 일 순서로 다시 줄 세우기(reindex)
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(df.groupby("요일")["매출"].sum().reindex(weekday_order))
# between: 9월 10 ~ 12일 사이의 행만
print(df[df["판매일"].between("2026-09-10", "2026-09-12")])
