# 자주 쓰는 문자열 메서드
s = "  Hello Python World  "
print("[" + s.strip() + "]")       # 양쪽 공백 제거
t = s.strip()
print(t.upper())                   # 대문자로
print(t.lower())                   # 소문자로
print(t.replace("World", "파이썬"))  # 바꾸기
print(t.split())                   # 공백 기준으로 나누기 → 리스트
print(t.find("Python"))            # 찾은 위치 (없으면 -1)
print(t.count("o"))                # 개수 세기
print(t.startswith("Hello"))       # ~로 시작하는가?

fruits = "사과,바나나,포도"
print(fruits.split(","))           # 쉼표 기준으로 나누기
print("-".join(["2026", "10", "04"]))   # 리스트를 이어 붙이기
