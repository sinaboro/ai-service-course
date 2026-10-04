# 실습용 데이터 만들기: 한글 엑셀 CSV(cp949) 와 큰 로그 파일
# (이미 data 폴더에 있다면 다시 실행할 필요 없어요)
import csv
import random
from pathlib import Path

# 데이터를 저장할 data 폴더 (없으면 만들기)
DATA = Path(__file__).parent / "data"
DATA.mkdir(exist_ok=True)

# 1) 엑셀에서 "CSV (쉼표로 분리)" 로 저장한 것 같은 파일 → cp949 인코딩
# 첫 줄 = 열 이름 / seed 고정으로 매번 같은 데이터
rows = [["판매일", "지점", "상품", "수량", "단가"]]
random.seed(7)
stores = ["강남점", "홍대점", "잠실점"]
items = [("아메리카노", 4000), ("카페라떼", 4500), ("치즈케이크", 6500), ("쿠키", 2500)]
# 9월 1 ~ 30일, 하루 2건씩: 날짜는 "2026.09.01" 모양, 단가는 "4,000" 처럼 쉼표 넣은 글자
for day in range(1, 31):
    for _ in range(2):
        name, price = random.choice(items)
        rows.append([f"2026.09.{day:02d}", random.choice(stores), name,
                     random.randint(1, 20), f"{price:,}"])
# encoding="cp949": 한글 윈도우 엑셀이 쓰는 방식으로 저장 / newline="": 빈 줄이 생기지 않게
with open(DATA / "sales_excel_cp949.csv", "w", encoding="cp949", newline="") as f:
    csv.writer(f).writerows(rows)

# 2) 2만 줄짜리 웹 접속 로그
random.seed(42)
pages = ["/home", "/product", "/cart", "/event", "/mypage"]
with open(DATA / "big_log.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["log_id", "user_id", "page", "seconds"])
    # 1 ~ 20000 번 로그: 사용자(u001 ~ u500), 페이지, 머문 시간(초)
    for i in range(1, 20001):
        w.writerow([i, f"u{random.randint(1, 500):03d}", random.choice(pages), random.randint(1, 300)])

# 만든 파일 이름과 크기 확인
for p in sorted(DATA.glob("*.csv")):
    print(f"{p.name:24} {p.stat().st_size:>8,} bytes")
