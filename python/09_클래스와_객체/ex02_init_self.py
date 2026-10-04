# __init__: 객체가 만들어질 때 자동으로 실행되는 메서드(생성자)
class Student:
    def __init__(self, name, kor, eng):
        self.name = name        # self.속성 = 값 → 객체에 저장
        self.kor = kor
        self.eng = eng

    def average(self):          # 메서드: 클래스 안의 함수
        return (self.kor + self.eng) / 2

    def __str__(self):          # print(객체) 했을 때 보일 모양
        return f"Student({self.name}, 평균 {self.average()})"

s1 = Student("홍길동", 90, 80)
s2 = Student("이순신", 70, 95)
print(s1.name, s1.average())
print(s2.name, s2.average())
print(s1)
