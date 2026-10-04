# 은행 계좌: 메서드로 데이터를 안전하게 바꾸기
class Account:
    bank = "파이썬은행"                 # 클래스 변수: 모든 계좌가 공유

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("0원 이하는 입금할 수 없어요.")
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족해요.")
            return
        self.balance -= amount

    def __str__(self):
        return f"[{Account.bank}] {self.owner}: {self.balance:,}원"

a = Account("홍길동", 10000)
b = Account("이순신")
a.deposit(5000)
a.withdraw(30000)
b.deposit(-100)
b.deposit(20000)
print(a)
print(b)
