# 은행 계좌: 메서드로 데이터를 안전하게 바꾸기
class Account:
    bank = "파이썬은행"                 # 클래스 변수: 모든 계좌가 공유

    # 계좌를 만들 때 주인 이름과 처음 잔액(기본 0원)을 받아요
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # 입금: 0원 이하면 안내만 하고 return 으로 바로 끝내기
    def deposit(self, amount):
        if amount <= 0:
            print("0원 이하는 입금할 수 없어요.")
            return
        self.balance += amount

    # 출금: 잔액보다 많이 꺼내려 하면 막기
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액이 부족해요.")
            return
        self.balance -= amount

    # print(객체) 할 때 보여 줄 글자 ({:,} 는 천 단위 쉼표)
    def __str__(self):
        return f"[{Account.bank}] {self.owner}: {self.balance:,}원"

# 계좌 두 개 만들기 (b 는 잔액을 안 줘서 0원)
a = Account("홍길동", 10000)
b = Account("이순신")
# 잔액 부족 · 음수 입금은 메서드가 막아 줘요
a.deposit(5000)
a.withdraw(30000)
b.deposit(-100)
b.deposit(20000)
print(a)
print(b)
