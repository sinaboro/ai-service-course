from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

path = DATA / "big_log.csv"

print(pd.read_csv(path, nrows=3))                     # 앞부분만 살짝 보기

# 한 번에 다 읽기
full = pd.read_csv(path)
print("전체 행 수:", len(full))

# 5000 줄씩 나눠 읽으면서 집계 (메모리가 부족할 때)
total = None
for i, chunk in enumerate(pd.read_csv(path, chunksize=5000), start=1):
    part = chunk.groupby("page")["seconds"].agg(["sum", "count"])
    total = part if total is None else total.add(part, fill_value=0)
    print(f"{i}번째 조각: {len(chunk)}줄")

total["avg_seconds"] = (total["sum"] / total["count"]).round(1)
print(total.sort_values("count", ascending=False))

# 두 방법의 결과가 같은지 확인
check = full.groupby("page")["seconds"].mean().round(1)
print("결과 일치:", (check == total["avg_seconds"]).all())

# 필요한 열 + 작은 자료형으로 읽어 메모리 줄이기
small = pd.read_csv(path, usecols=["page", "seconds"], dtype={"page": "category", "seconds": "int16"})
print(f"메모리: {full.memory_usage(deep=True).sum() // 1024:,} KB → {small.memory_usage(deep=True).sum() // 1024:,} KB")
