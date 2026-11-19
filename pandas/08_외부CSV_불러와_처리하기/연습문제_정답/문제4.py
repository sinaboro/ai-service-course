# 문제 4. data/monthly 폴더의 모든 CSV를 합쳐서 상품별 총 판매 수량을 많은 순으로 출력하세요.

from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import pandas as pd  # 판다스 (관례적으로 pd 라는 별명)

# 정답 파일은 "연습문제_정답" 폴더 안에 있고, data 폴더는 한 단계 위(예제 폴더)에 있어요.
# 그래서 이 파일의 위치를 기준으로 경로를 만들어요. (어느 폴더에서 실행해도 동작 — 1-2절)
DATA = Path(__file__).parent.parent / "data"

files = sorted((DATA / "monthly").glob("*.csv"))
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)  # 파일마다 읽은 표들을 위아래로 합치기
print(df.groupby("product")["qty"].sum().sort_values(ascending=False))
