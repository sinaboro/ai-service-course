# 문제 3. words = ["apple", "hi", "banana", "ok", "python"]에서 3글자 이상인 단어만 컴프리헨션으로 모으세요.

words = ["apple", "hi", "banana", "ok", "python"]
long_words = [w for w in words if len(w) >= 3]
print(long_words)
