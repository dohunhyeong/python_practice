import random
from abc import ABC, abstractmethod


# BankAccount 클래스가 추상클래스임을 명시
# 그리고 그 중에서도 info 라는 메서드는 추상메서드임.
class BankAccount(ABC):
    def __init__(self, holder_name, balance):
        self._account_number = random.randint(10000000, 99999999)
        self._holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("잔액이 부족합니다.")
        else:
            self.__balance -= amount
            return self.__balance

    @abstractmethod
    def info(self):
        pass


class SavingAccount(BankAccount):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.__interest_rate = interest_rate
        self.__is_locked = True

    def withdraw(self, amount):
        if self.__is_locked == True:
            raise AttributeError
        else:
            return super().withdraw(amount)
