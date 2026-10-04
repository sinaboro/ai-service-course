# type() 과 isinstance() 로 자료형 확인하기
values = [10, 3.14, "hello", True, [1, 2], {"a": 1}, None]

for v in values:
    print(f"{str(v):10} → type: {type(v).__name__:8} | int 인가? {isinstance(v, int)}")

# 같은 자료형인지 비교
x = 5
print(type(x) == int)              # True
print(isinstance(x, int))          # True

# 여러 자료형 중 하나인지: 튜플로 묶어서
print(isinstance(3.0, (int, float)))     # 숫자인가?
print(isinstance("3", (int, float)))

# 주의: bool 은 int 의 자식이에요!
print(isinstance(True, int))       # True  ← 놀랍죠?
print(type(True) == int)           # False
