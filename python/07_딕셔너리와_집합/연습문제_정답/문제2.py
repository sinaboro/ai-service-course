# 문제 2. 문자열 "banana"에서 각 글자가 몇 번 나오는지 딕셔너리로 세어 출력하세요.

word = "banana"
count = {}
for ch in word:
    count[ch] = count.get(ch, 0) + 1
print(count)
