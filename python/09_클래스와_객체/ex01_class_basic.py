# 클래스 없이 학생 정보를 관리하면 변수가 흩어져요
name1, kor1, eng1 = "홍길동", 90, 80
name2, kor2, eng2 = "이순신", 70, 95

# 클래스: 설계도
class Student:
    pass                      # 아직 내용 없음

s1 = Student()                # 객체(인스턴스) 만들기
s1.name = "홍길동"             # 객체에 속성 붙이기
s1.kor = 90
s2 = Student()
s2.name = "이순신"

print(s1.name, s1.kor)
print(s2.name)
print(type(s1))
