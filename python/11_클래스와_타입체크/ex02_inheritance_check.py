# 상속 관계에서의 타입 확인
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
print(type(d) == Dog)            # True
print(type(d) == Animal)         # False  ← type() 은 "정확히" 같아야 함
print(isinstance(d, Dog))        # True
print(isinstance(d, Animal))     # True   ← isinstance 는 부모도 인정
print(isinstance(d, Cat))        # False

print(issubclass(Dog, Animal))   # 클래스끼리: Dog 는 Animal 의 자식인가?
print(issubclass(Animal, Dog))
print(Dog.__mro__)               # 상속 순서 (부모를 찾아가는 순서)
