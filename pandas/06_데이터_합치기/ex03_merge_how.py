import pandas as pd

students = pd.DataFrame({"id": [1, 2, 3, 4], "name": ["Kim", "Lee", "Park", "Choi"]})
scores = pd.DataFrame({"id": [1, 2, 3, 5], "score": [90, 85, 77, 60]})

print("inner (양쪽에 다 있는 것)")
print(pd.merge(students, scores, on="id", how="inner"))
print("left (왼쪽 기준)")
print(pd.merge(students, scores, on="id", how="left"))
print("right (오른쪽 기준)")
print(pd.merge(students, scores, on="id", how="right"))
print("outer (전부)")
print(pd.merge(students, scores, on="id", how="outer"))

# 열 이름이 서로 다르면 left_on / right_on
orders = pd.DataFrame({"student_id": [1, 1, 3], "book": ["Python", "NumPy", "pandas"]})
print(pd.merge(students, orders, left_on="id", right_on="student_id"))
