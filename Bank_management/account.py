import random
from abc import ABC, abstractmethod


# 입출금 계좌, 예금계좌가 있기 때문에 이 두 계좌의 공통적인 특징을 뽑아서 추상화할 수 있다는 아이디어에서 비롯됨.
# BankAccount 클래스가 추상클래스임을 명시
# 그리고 그 중에서도 info 라는 메서드는 추상메서드임.
class BankAccount(ABC):
    def __init__(self, holder_name, balance):
        self._account_number = random.randint(10000000, 99999999)
        # holder_name(예금주) 멤버변수는 protected_field로 설정('_')
        self._holder_name = holder_name
        # balance(잔액)은 민감한 정보이기 때문에 private field로 설정('__')
        self.__balance = balance
    def get_account_number(self):
        return self._account_number    

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

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
            raise AttributeError('출금이 제한되었습니다.')
        else:
            return super().withdraw(amount)

    # 출금 제한 해제
    def unlock(self):
        # interest = self.__balance* self.__interest_rate
        # 이때, self.__balance 는 BankAccount의 변수입니다. 그러나 "__"로 되어있는 변수는 아무리 상속 관계라고 하더라도 가져올 수가 없습니다.
        # 그렇기 때문에 위에서 BankAccount() 클래스의 balance를 가져올 수 있는  get 메서드를 BankAccount 클래스에 구현하고 
        # 이것을통해서 balance를 가져올 수 있도록 해야함.
        self.__is_locked =False
        interest = self.get_balance() * self.__interest_rate
        print(interest)
        self.deposit(interest)

    def info(self):
        print(f"[예금/{self.get_account_number()}] 잔액 ${self.get_balance()} , 이율{self.__interest_rate}, 출금제한여부{self.__is_locked}")

class CheckingAccount(BankAccount):
    def __init__(self, holder_name, balance, withdraw_limit =500):
        super().__init__(holder_name, balance)
        self.__withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if (self.__withdraw_limit<amount):
            raise ValueError
        else:
            super().withdraw(amount)

    # 출금 제한 한도를 변경하는 코드
    def update_limit(self, new_limit):
        self.__withdraw_limit = new_limit
    
    def info(self):
        print(f"[입출금/ {self.get_account_number()}], 잔액 {self.get_balance()}, 출금한도{self.__withdraw_limit}")