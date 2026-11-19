# 문제 5. data/big_log.csv를 chunksize=4000으로 나눠 읽으면서 /cart 페이지의 접속 횟수를 세어 출력하세요.

from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import pandas as pd  # 판다스 (관례적으로 pd 라는 별명)

# 정답 파일은 "연습문제_정답" 폴더 안에 있고, data 폴더는 한 단계 위(예제 폴더)에 있어요.
# 그래서 이 파일의 위치를 기준으로 경로를 만들어요. (어느 폴더에서 실행해도 동작 — 1-2절)
DATA = Path(__file__).parent.parent / "data"

count = 0
for chunk in pd.read_csv(DATA / "big_log.csv", chunksize=4000):
    count += (chunk["page"] == "/cart").sum()
print("/cart 접속 횟수:", count)
