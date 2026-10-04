from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

df = pd.read_csv(
    DATA / "survey_messy.csv",
    na_values=["-", "N/A", "unknown"],   # 이 글자들은 빈 값(NaN)으로
    thousands=",",
    skipinitialspace=True,               # 쉼표 뒤 공백 무시
)
print("원본:")
print(df)

# 1) 열 이름의 공백 제거
df.columns = df.columns.str.strip()
# 2) 문자열 값의 앞뒤 공백 제거
for col in ["응답자", "지역"]:
    df[col] = df[col].str.strip()
# 3) "25세" → 25 (숫자만 뽑기)
df["나이"] = df["나이"].str.extract(r"(\d+)", expand=False).astype("Int64")
# 4) 표기 통일: M/F → 남/여
df["성별"] = df["성별"].replace({"M": "남", "F": "여"})
# 5) 중복 행 제거
df = df.drop_duplicates()
# 6) 빈 값 확인 후 채우기
print("\n빈 값 개수:")
print(df.isna().sum())
df["만족도"] = df["만족도"].fillna(df["만족도"].median())

print("\n정리 후:")
print(df)
print(df.dtypes)
print("\n지역별 평균 구매금액:")
print(df.groupby("지역")["구매금액"].mean().round(0))
