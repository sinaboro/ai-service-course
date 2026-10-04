# 문제 2. 리스트를 받아 짝수만 담은 새 리스트를 돌려주는 함수 evens(nums)를 만드세요.

def evens(nums):
    return [n for n in nums if n % 2 == 0]

print(evens([1, 2, 3, 4, 5, 6]))
