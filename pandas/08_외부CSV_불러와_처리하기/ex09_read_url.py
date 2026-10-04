from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

try:
    tips = pd.read_csv(URL)                       # 인터넷 주소에서 바로 읽기
    print("인터넷에서 읽기 성공")
except Exception as e:                            # 인터넷이 안 되면
    print("인터넷 연결 실패 → 백업 파일 사용:", type(e).__name__)
    tips = pd.read_csv(DATA / "tips_backup.csv")

print(tips.shape)
print(tips.head())

tips["tip_rate(%)"] = (tips["tip"] / tips["total_bill"] * 100).round(1)
print(tips.groupby("day")["tip_rate(%)"].mean().round(2).sort_values(ascending=False))
print(tips.pivot_table(index="time", columns="smoker", values="tip", aggfunc="mean").round(2))
