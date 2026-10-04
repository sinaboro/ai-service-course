# for 와 range()
for i in range(5):           # 0, 1, 2, 3, 4
    print("반복", i)

print(list(range(1, 6)))     # 1 ~ 5
print(list(range(0, 11, 2))) # 0 ~ 10, 2씩
print(list(range(5, 0, -1))) # 5 ~ 1, 거꾸로

# 문자열의 글자를 하나씩
for ch in "파이썬":
    print(ch)
