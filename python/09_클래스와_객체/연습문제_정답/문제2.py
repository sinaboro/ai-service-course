# 문제 2. Book 클래스에 제목과 가격을 저장하고, __str__로 print(책) 하면 "《제목》 15,000원"처럼 나오게 하세요.

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"《{self.title}》 {self.price:,}원"

print(Book("파이썬 첫걸음", 15000))
