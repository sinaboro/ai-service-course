# 상속: 부모 클래스의 기능을 물려받기
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}이(가) 밥을 먹어요.")

    def sound(self):
        print("...")

class Dog(Animal):                 # Animal 을 상속
    def sound(self):               # 오버라이딩: 다시 정의
        print(f"{self.name}: 멍멍!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)     # 부모의 __init__ 호출
        self.color = color

    def sound(self):
        print(f"{self.color} {self.name}: 야옹~")

animals = [Dog("바둑이"), Cat("나비", "노란")]
for a in animals:
    a.eat()        # 물려받은 메서드
    a.sound()      # 각자 다르게 동작 (다형성)
