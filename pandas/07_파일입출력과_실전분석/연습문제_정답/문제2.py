# 문제 2. Americano의 날짜별 판매 수량 합계를 구하세요.

from pathlib import Path
import pandas as pd

# 정답 파일은 "연습문제_정답" 폴더 안에 있고, cafe_sales.csv 는 한 단계 위(예제 폴더)에 있어요.
# 그래서 이 파일의 위치를 기준으로 경로를 만들어요. (어느 폴더에서 실행해도 동작 — 8장 1-2절)
HERE = Path(__file__).parent.parent

df = pd.read_csv(HERE / "cafe_sales.csv")
ame = df[df["product"] == "Americano"]
print(ame.groupby("date")["qty"].sum().astype(int))
