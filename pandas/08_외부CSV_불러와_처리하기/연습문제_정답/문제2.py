# 문제 2. data/sales_excel_cp949.csv를 읽어 지점별 판매 수량 합계를 구하세요.

import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

df = pd.read_csv("data/sales_excel_cp949.csv", encoding="cp949", thousands=",")
print(df.groupby("지점")["수량"].sum())
