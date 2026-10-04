import pandas as pd

students = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Kim", "Lee", "Park", "Choi"],
})
scores = pd.DataFrame({
    "id": [1, 2, 3, 5],
    "score": [90, 85, 77, 60],
})

merged = pd.merge(students, scores, on="id")    # id 가 같은 행끼리 연결
print(merged)
