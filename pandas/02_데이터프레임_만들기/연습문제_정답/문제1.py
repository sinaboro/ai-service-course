# 문제 1. 상품(product), 가격(price), 재고(stock) 열을 가진 DataFrame을 만드세요. 데이터: (Pen, 1500, 30), (Note, 3000, 12), (Bag, 25000, 5)

import pandas as pd
df = pd.DataFrame({
    "product": ["Pen", "Note", "Bag"],
    "price": [1500, 3000, 25000],
    "stock": [30, 12, 5],
})
print(df)
