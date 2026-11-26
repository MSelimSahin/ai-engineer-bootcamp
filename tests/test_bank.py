import pytest
from day06.bank import BankAccount, InsufficientFundsError

def test_deposit_increases_balance():
    acc = BankAccount("Selim", 100)
    acc.deposit(50)
    assert acc.balance == 150

def test_deposit_rejects_zero():
    acc = BankAccount("Selim")
    with pytest.raises(ValueError):
        acc.deposit(0)

def test_withdraw_decreases_balance():
    acc = BankAccount("Selim", 100)
    acc.withdraw(50)
    assert acc.balance == 50

def test_insufficient_funds():
    acc = BankAccount("Selim", 200)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(500)

def test_failed_transaction():
    acc = BankAccount("Selim", 100)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(500)
    assert acc.history == []
    assert acc.balance == 100

def test_account_independency():
    acc = BankAccount("Selim", 200)
    acc2 = BankAccount("KOC", 100)
    acc.deposit(100)
    assert acc.balance == 300
    assert acc2.balance == 100

def test_repr_function():
    acc = BankAccount("Selim", 200)
    assert repr(acc) == "BankAccount(owner='Selim', balance=200.00)"

def test_start_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("Selim", -100)