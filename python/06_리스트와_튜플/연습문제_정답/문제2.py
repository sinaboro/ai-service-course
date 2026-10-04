# 문제 2. 빈 리스트에 1부터 5까지 append로 넣고, 거꾸로 정렬해서 출력하세요.

nums = []
for i in range(1, 6):
    nums.append(i)
nums.sort(reverse=True)
print(nums)
