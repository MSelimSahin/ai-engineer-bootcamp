class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
        if self.balance < 0:
                    raise ValueError(f"Starting balance could not be negative, got {self.balance}")

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.balance:.2f})"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive, got {amount}")
        self.balance += amount
        self.history.append(("deposit", amount))
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"Withdraw amount must be positive, got {amount}")
        elif amount > self.balance:
            raise InsufficientFundsError(f"Balance is {self.balance}, cannot withdraw {amount}")
        self.balance -= amount
        self.history.append(("withdraw", amount))
        return self.balance


if __name__ == "__main__":

    p1 = BankAccount("Selim", 200)
    print(p1.deposit(100))
    print(p1.withdraw(50))
    print(repr(p1))
    print(p1.history)
    p2 = BankAccount("KOC", 100)
    print(p2.history)

    def expect_error(error_type, func, *args):
         try:
              func(*args)
         except error_type:
              return
         raise AssertionError(f"{func.__name__}{args} should have raised {error_type.__name__}")

    expect_error(ValueError, p1.deposit, 0)
    expect_error(ValueError, p1.deposit, -50)
    expect_error(InsufficientFundsError, p1.withdraw, 500)
    expect_error(ValueError, p1.withdraw, 0)
    expect_error(ValueError, p1.withdraw, -50)