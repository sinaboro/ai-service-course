# 문제 1. describe(x) 함수를 만들어 x가 bool이면 "불", int면 "정수", float면 "실수", str면 "문자열", 그 밖에는 "기타"를 반환하세요. [True, 7, 2.5, "a", None]로 테스트하세요.

def describe(x):
    if isinstance(x, bool):
        return "불"
    elif isinstance(x, int):
        return "정수"
    elif isinstance(x, float):
        return "실수"
    elif isinstance(x, str):
        return "문자열"
    return "기타"

for v in [True, 7, 2.5, "a", None]:
    print(f"{v!r} → {describe(v)}")
