from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

# 종합 실습: 엑셀에서 받은 매출 CSV → 정리 → 분석 → 보고서 CSV 저장
SRC = DATA / "sales_excel_cp949.csv"
OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

# 1) 읽기
df = pd.read_csv(SRC, encoding="cp949", thousands=",")
print(f"[1] 읽기: {len(df)}행 {df.shape[1]}열")

# 2) 정리
df["판매일"] = pd.to_datetime(df["판매일"], format="%Y.%m.%d")
df["매출"] = df["수량"] * df["단가"]
# 중복 행 제거 전후 개수를 비교해서 몇 행 지웠는지 출력
before = len(df)
df = df.drop_duplicates()
print(f"[2] 정리: 중복 {before - len(df)}행 제거, 빈 값 {int(df.isna().sum().sum())}개")

# 3) 분석
total = df["매출"].sum()
# 지점별 매출 · 판매 수량 + 전체 매출 중 비중(%)
by_store = df.groupby("지점", as_index=False).agg(매출=("매출", "sum"), 판매수량=("수량", "sum"))
by_store["비중(%)"] = (by_store["매출"] / total * 100).round(1)
by_store = by_store.sort_values("매출", ascending=False)
# 상품별 매출, 매출이 가장 큰 날(idxmax: 최댓값의 인덱스 = 날짜)
by_item = df.groupby("상품")["매출"].sum().sort_values(ascending=False)
best_day = df.groupby("판매일")["매출"].sum().idxmax()

print(f"[3] 총매출 {total:,}원 / 최고 매출일 {best_day.date()}")
print(by_store)
print(by_item)

# 4) 저장 (엑셀에서 한글이 깨지지 않게 utf-8-sig)
by_store.to_csv(OUT / "report_by_store.csv", index=False, encoding="utf-8-sig")
by_item.to_csv(OUT / "report_by_item.csv", encoding="utf-8-sig")
print("[4] 저장:", sorted(p.name for p in OUT.glob("report_*.csv")))

# 저장한 파일을 다시 읽어 확인
print(pd.read_csv(OUT / "report_by_store.csv", encoding="utf-8-sig"))
