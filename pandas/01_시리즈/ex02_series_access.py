# ex02_series_access.py : Series 에서 값 꺼내기: 라벨 s["kim"] · 위치 s.iloc[0] · 여러 개 · 슬라이싱
import pandas as pd              # 판다스 (관례적으로 pd 라는 별명)

score = pd.Series([90, 75, 88, 62], index=["kim", "lee", "park", "choi"])

print(score["lee"])              # 라벨로 꺼내기
print(score.iloc[0])             # 위치(순서)로 꺼내기
print(score[["kim", "park"]])    # 여러 개 → Series
print(score["lee":"choi"])       # 라벨 슬라이싱 (끝 포함!)

score["lee"] = 80                # 값 바꾸기
score["jung"] = 95               # 새 라벨 추가
print(score)
print("kim" in score)            # 라벨이 있는지
