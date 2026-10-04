import pandas as pd

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi", "Jung"],
    "dept": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [4500, 3800, 5200, 4100, 4500],
})

print(df.sort_values("salary"))                         # 오름차순
print(df.sort_values("salary", ascending=False))        # 내림차순
print(df.sort_values(["dept", "salary"], ascending=[True, False]))   # 부서 → 연봉 높은 순
print(df.nlargest(2, "salary"))                         # 상위 2개
df["rank"] = df["salary"].rank(ascending=False, method="min").astype(int)   # 순위
print(df)
