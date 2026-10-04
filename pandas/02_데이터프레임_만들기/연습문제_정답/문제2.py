# 문제 2. 문제 1의 DataFrame에서 product를 인덱스로 만들고 shape를 출력하세요.

import pandas as pd
df = pd.DataFrame({"product": ["Pen", "Note", "Bag"], "price": [1500, 3000, 25000], "stock": [30, 12, 5]})
df = df.set_index("product")
print(df.shape)
