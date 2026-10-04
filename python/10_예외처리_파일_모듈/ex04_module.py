# 모듈 가져다 쓰기
import math
import random
from datetime import date
import mytools                      # 같은 폴더의 mytools.py

print(math.sqrt(16), math.pi)
print(math.ceil(3.2), math.floor(3.8))

random.seed(42)                     # 난수를 매번 같게 (실습용)
print(random.randint(1, 6))         # 1 ~ 6 정수
print(random.choice(["가위", "바위", "보"]))

print(date(2026, 10, 4).weekday())   # 0=월 ... 6=일

print(mytools.circle_area(2))
print(mytools.won(1500000))
