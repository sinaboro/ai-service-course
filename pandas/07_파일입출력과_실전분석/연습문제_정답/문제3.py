# 문제 3. 매장(store)별 총매출을 구해 store_total.csv로 저장한 뒤, 다시 읽어서 출력하세요.

from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import pandas as pd  # 판다스 (관례적으로 pd 라는 별명)

# 정답 파일은 "연습문제_정답" 폴더 안에 있고, cafe_sales.csv 는 한 단계 위(예제 폴더)에 있어요.
# 그래서 이 파일의 위치를 기준으로 경로를 만들어요. (어느 폴더에서 실행해도 동작 — 8장 1-2절)
HERE = Path(__file__).parent.parent

df = pd.read_csv(HERE / "cafe_sales.csv")
df["qty"] = df["qty"].fillna(0).astype(int)
df["amount"] = df["qty"] * df["price"]
total = df.groupby("store", as_index=False)["amount"].sum()
total.to_csv(HERE / "store_total.csv", index=False, encoding="utf-8-sig")
print(pd.read_csv(HERE / "store_total.csv"))
