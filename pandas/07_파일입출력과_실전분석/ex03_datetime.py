# ex03_datetime.py : 날짜 다루기: parse_dates · .dt.year · .dt.day_name() · strftime
import pandas as pd                            # 판다스 (관례적으로 pd 라는 별명)

df = pd.read_csv("cafe_sales.csv", parse_dates=["date"])   # 읽으면서 날짜로
print(df["date"].dtype)

df["day"] = df["date"].dt.day                  # 일
df["weekday"] = df["date"].dt.day_name()       # 요일 이름
print(df[["date", "day", "weekday"]].drop_duplicates().reset_index(drop=True))

print(df[df["date"] >= "2026-09-04"].shape)    # 날짜로 필터
