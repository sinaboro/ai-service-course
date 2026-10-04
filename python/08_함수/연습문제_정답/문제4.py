# 문제 4. words = ["banana", "kiwi", "apple", "fig"]를 글자 수가 짧은 순으로 lambda를 이용해 정렬하세요.

words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words, key=lambda w: len(w)))
