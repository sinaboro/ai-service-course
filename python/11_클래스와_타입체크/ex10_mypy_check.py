# 이 파일은 실행은 되지만 타입 힌트와 맞지 않는 곳이 있어요.
# 터미널에서  python -m mypy ex10_mypy_check.py  로 검사해 보세요.
class Account:
    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

acc = Account("홍길동", 1000)
print(acc.deposit(500))

bad = Account(12345, "천원")      # owner 에 int, balance 에 str
print(bad.owner, bad.balance)
