# ex08_big_file.py : 큰 CSV 나눠 읽기: nrows(앞부분만) · usecols/dtype(메모리 절약) · chunksize(조각씩)
from pathlib import Path                                  # 파일 · 폴더 경로를 다루는 도구
import pandas as pd                                       # 판다스 (관례적으로 pd 라는 별명)

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
    # 첫 조각이면 그대로 저장, 다음부터는 이전 결과에 더하기 (fill_value=0: 한쪽에 없는 항목은 0 으로 보고 더함)
    total = part if total is None else total.add(part, fill_value=0)
    print(f"{i}번째 조각: {len(chunk)}줄")

total["avg_seconds"] = (total["sum"] / total["count"]).round(1)
print(total.sort_values("count", ascending=False))

# 두 방법의 결과가 같은지 확인
check = full.groupby("page")["seconds"].mean().round(1)
print("결과 일치:", (check == total["avg_seconds"]).all())    # 모든 값이 같으면 True

# 필요한 열 + 작은 자료형으로 읽어 메모리 줄이기
small = pd.read_csv(path, usecols=["page", "seconds"], dtype={"page": "category", "seconds": "int16"})
print(f"메모리: {full.memory_usage(deep=True).sum() // 1024:,} KB → {small.memory_usage(deep=True).sum() // 1024:,} KB")
