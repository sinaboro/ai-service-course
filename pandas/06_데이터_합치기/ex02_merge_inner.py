import pandas as pd

# 학생 표: id 1 ~ 4
students = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Kim", "Lee", "Park", "Choi"],
})
# 점수 표: id 1, 2, 3, 5 (4번은 점수 없음, 5번은 학생 목록에 없음)
scores = pd.DataFrame({
    "id": [1, 2, 3, 5],
    "score": [90, 85, 77, 60],
})

# 기본(how="inner"): 양쪽에 모두 있는 id(1, 2, 3)만 남아요
merged = pd.merge(students, scores, on="id")    # id 가 같은 행끼리 연결
print(merged)
