# 문제 5. data/big_log.csv를 chunksize=4000으로 나눠 읽으면서 /cart 페이지의 접속 횟수를 세어 출력하세요.

import pandas as pd

count = 0
for chunk in pd.read_csv("data/big_log.csv", chunksize=4000):
    count += (chunk["page"] == "/cart").sum()
print("/cart 접속 횟수:", count)
