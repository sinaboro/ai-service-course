# 문제 3. greet(name, lang="ko") 함수를 만들어 lang이 "ko"면 "안녕, 이름", "en"이면 "Hello, 이름"을 출력하세요.

def greet(name, lang="ko"):
    if lang == "ko":
        print(f"안녕, {name}")
    else:
        print(f"Hello, {name}")

greet("민수")
greet("Tom", lang="en")
