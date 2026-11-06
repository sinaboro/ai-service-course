# JSON 과 파이썬 딕셔너리 — 웹에서 데이터를 주고받는 글자 형식 익히기 (python 으로 실행)
# 서버는 파이썬 딕셔너리를 JSON 글자로 바꿔 보내고, 받는 쪽은 그 글자를 다시 딕셔너리로 바꿔요.
import json

# 1) 파이썬 딕셔너리 (내 프로그램 안에서 쓰는 값)
student = {"name": "홍길동", "age": 20, "scores": [90, 85], "is_member": True, "memo": None}
print("딕셔너리:", student)
print("타입:", type(student))

# 2) 딕셔너리 → JSON 글자 (서버가 응답을 보낼 때 하는 일)
#    ensure_ascii=False: 한글을 홍 같은 기호 대신 글자 그대로
text = json.dumps(student, ensure_ascii=False)
print("\nJSON 글자:", text)
print("타입:", type(text))                     # str — 네트워크로는 글자만 보낼 수 있어요

# 파이썬과 JSON 표기 차이: True → true, None → null, 작은따옴표 → 큰따옴표

# 3) JSON 글자 → 딕셔너리 (응답을 받은 쪽이 하는 일)
back = json.loads(text)
print("\n다시 딕셔너리:", back)
print("이름만 꺼내기:", back["name"])
print("첫 번째 점수:", back["scores"][0])

# 4) 보기 좋게 출력하기 (indent=2: 두 칸 들여쓰기) — 이 과정의 _client.py 파일들이 쓰는 방법
print("\n보기 좋게:")
print(json.dumps(student, ensure_ascii=False, indent=2))
