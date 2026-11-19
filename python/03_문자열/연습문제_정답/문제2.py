# 문제 2. word = "level"이 앞뒤로 읽어도 같은지(회문) True/False로 출력하세요.

word = "level"
print(word == word[::-1])  # [::-1] 은 거꾸로 뒤집은 문자열
