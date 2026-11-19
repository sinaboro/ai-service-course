# 문제 2. data/sales_excel_cp949.csv를 읽어 지점별 판매 수량 합계를 구하세요.

from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import pandas as pd  # 판다스 (관례적으로 pd 라는 별명)

# 정답 파일은 "연습문제_정답" 폴더 안에 있고, data 폴더는 한 단계 위(예제 폴더)에 있어요.
# 그래서 이 파일의 위치를 기준으로 경로를 만들어요. (어느 폴더에서 실행해도 동작 — 1-2절)
DATA = Path(__file__).parent.parent / "data"
pd.set_option("display.unicode.east_asian_width", True)

df = pd.read_csv(DATA / "sales_excel_cp949.csv", encoding="cp949", thousands=",")
print(df.groupby("지점")["수량"].sum())
