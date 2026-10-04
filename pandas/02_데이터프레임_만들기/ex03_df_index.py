import pandas as pd

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park"],
    "kor": [90, 75, 88],
    "eng": [85, 95, 70],
})

df2 = df.set_index("name")          # name 열을 인덱스로
print(df2)
print(df2.index.tolist())

print(df2.reset_index())            # 인덱스를 다시 열로

df3 = df.rename(columns={"kor": "korean", "eng": "english"})   # 열 이름 바꾸기
print(df3.columns.tolist())

df.columns = ["이름", "국어", "영어"]    # 열 이름 전체 바꾸기
print(df)
