# 딕셔너리: { 키: 값, 키: 값 }
student = {"name": "홍길동", "age": 20, "major": "컴퓨터"}

print(student["name"])          # 키로 값 꺼내기
student["age"] = 21             # 값 바꾸기
student["grade"] = "A"          # 새 키 추가
print(student)

del student["major"]            # 삭제
print(student)
print(len(student))             # 키의 개수
print("age" in student)         # 키가 있는지 확인

print(student.get("phone"))             # 없는 키 → None (오류 아님)
print(student.get("phone", "없음"))      # 없을 때 기본값
