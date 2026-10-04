# 자료형 변환
s = "123"
n = int(s)            # 문자열 → 정수
print(n + 1)

f = float("3.5")      # 문자열 → 실수
print(f * 2)

print(int(3.99))      # 실수 → 정수 (소수점 버림)
print(round(3.99))    # 반올림

age = 20
msg = "나이: " + str(age)   # 정수 → 문자열
print(msg)

print(bool(0), bool(1), bool(""), bool("a"))
