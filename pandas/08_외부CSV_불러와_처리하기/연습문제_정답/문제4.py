# 문제 4. data/monthly 폴더의 모든 CSV를 합쳐서 상품별 총 판매 수량을 많은 순으로 출력하세요.

from pathlib import Path
import pandas as pd

files = sorted(Path("data/monthly").glob("*.csv"))
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
print(df.groupby("product")["qty"].sum().sort_values(ascending=False))
