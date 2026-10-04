from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

files = sorted((DATA / "monthly").glob("sales_*.csv"))   # 패턴에 맞는 파일 모두
print([f.name for f in files])

# 파일마다 읽어서 목록(frames)에 모으기 (parse_dates: date 열을 날짜로)
frames = []
for f in files:
    part = pd.read_csv(f, parse_dates=["date"])
    part["source"] = f.stem                 # 어느 파일에서 왔는지 기록
    frames.append(part)

# concat: 여러 표를 위아래로 이어 붙이기 (ignore_index: 행 번호 새로 매기기)
df = pd.concat(frames, ignore_index=True)
df["amount"] = df["qty"] * df["price"]
print(df.shape)
print(df.tail(4))

# 날짜 → "2026-07" 같은 월 글자 → 월별 · 상품별 피벗
df["month"] = df["date"].dt.strftime("%Y-%m")
print(df.pivot_table(index="month", columns="product", values="amount",
                     aggfunc="sum", fill_value=0, margins=True, margins_name="합계"))
