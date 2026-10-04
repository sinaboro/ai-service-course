# 문제 3. 문제 1의 DataFrame에서 price 열 이름을 price_won으로 바꾸고 열 이름 목록을 출력하세요.

import pandas as pd
df = pd.DataFrame({"product": ["Pen", "Note", "Bag"], "price": [1500, 3000, 25000], "stock": [30, 12, 5]})
df = df.rename(columns={"price": "price_won"})
print(df.columns.tolist())
