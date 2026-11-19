# ex01_add_drop.py : 열 추가(계산해서) · 칸 수정(loc) · 행 · 열 삭제(drop)
import pandas as pd                             # 판다스 (관례적으로 pd 라는 별명)

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park"],
    "kor": [90, 75, 88],
    "eng": [85, 95, 70],
})

df["math"] = [80, 65, 92]                       # 새 열 (리스트)
df["total"] = df["kor"] + df["eng"] + df["math"]  # 계산한 새 열
df["avg"] = (df["total"] / 3).round(1)
df["pass"] = df["avg"] >= 80                    # 조건 결과를 열로
print(df)

df.loc[df["name"] == "Lee", "eng"] = 100        # 조건에 맞는 칸만 바꾸기
print(df.loc[1])

print(df.drop(columns=["pass"]))                # 열 삭제 (새 DataFrame)
print(df.drop(index=0))                         # 0 번 행 삭제
