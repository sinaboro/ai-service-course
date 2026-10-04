from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

path = DATA / "sales_excel_cp949.csv"

# 1) 기본(utf-8)으로 읽으면?
try:
    pd.read_csv(path)
except UnicodeDecodeError as e:
    print("utf-8 로 읽기 실패:", type(e).__name__)

# 2) 한글 윈도우 엑셀 파일은 cp949 (또는 euc-kr)
df = pd.read_csv(path, encoding="cp949")
print(df.head(3))

# 3) 인코딩을 모를 때: 차례로 시도하는 함수
def read_csv_auto(p, encodings=("utf-8", "utf-8-sig", "cp949")):
    for enc in encodings:
        try:
            result = pd.read_csv(p, encoding=enc)
            print(f"{p.name} → {enc} 로 읽기 성공")
            return result
        except UnicodeDecodeError:
            continue
    raise ValueError("알려진 인코딩으로 읽을 수 없어요")

read_csv_auto(DATA / "students.csv")
read_csv_auto(path)
