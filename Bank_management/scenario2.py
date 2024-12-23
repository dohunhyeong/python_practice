from account import SavingAccount, CheckingAccount
from user import BankUser

user2 = BankUser('binsu', 900)
user2.deduct_money(100)
account_saving = SavingAccount(user2.get_name(), 100, 0.06)
user2.add_accounts(account_saving)

user2.deduct_money(800)
account_using = CheckingAccount(user2.get_name(),800)
user2.add_accounts(account_using)

try:
    account_using.withdraw(800)
except ValueError:
    account_using.update_limit(800)
    account_using.withdraw(800)
finally:
    user2.add_money(800)

user2.get_assets()

