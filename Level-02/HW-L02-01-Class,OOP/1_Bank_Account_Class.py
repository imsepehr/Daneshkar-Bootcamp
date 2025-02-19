from abc import abstractmethod, ABC
class Account(ABC):
    def __init__(
            self, 
            b: float ,
            n: str,
    ):
        self.balance, self.number = b, n
        self. __transactions = []

    def deposit(self, money : float):
        self.balance += money
        self.__transactions.append(money)

    def withdraw(self, money : float):
        self.balance -= money
        self.__transactions.append(-1 * money)

    def show_balance(self):
        return self.balance
    
    def __repr__(self) -> str:
        return f"{self.number} : {round(self.balance, 2)}"
    
    @property
    def transactions(self):
        return self.__transactions



class CheckingAccount(Account):
    min_amount = 50
    def __init__(self):
        if self.balance < self.min_amount:
            raise Exception("Balance below minimum amount")
        
    def __str__(self) -> str:
        return f"Checking Account, Number: {self.number}, Balance: {self.balance}"


class SavingAccount(Account):
    def income_expenses_ratio(self):
        income , expenses = 0
        for i in self.__transactions:
            if i < 0:
                expenses += i
            else:
                income += i
        return income/expenses
    
    def __str__(self) -> str:
        return f"Saving Account, Number: {self.number}, Balance: {self.balance}"
    
class CurrencyAccount(Account):
    dollars_fee = 600_000  #rial

    @staticmethod
    def convertor(self):
        return self.balance / self.dollars_fee
    
    def show_transactions(self):
        res = [i/self.dollars_fee for i in self.__transactions]
        print(res)

    def __str__(self) -> str:
        return f"Business Account, Number: {self.number}, Balance: {self.balance}"



# account1 = Account(100.256, 1273752910)
# account1.deposit(150)
# print(account1)
# account1.withdraw(50)
# print(account1)
# print(account1.transactions)


class Costumer():
    def __init__(self,
                 name : str,
                 ssn : str,
                 acc_type = 'C' | 'S' | 'B'
    ):
        self.name = name,
        self.ssn = ssn

    def checking_open_account(self, num, bal):
        new_account = CheckingAccount(450, 123456)

    def saving_open_account(self, num, bal):
        new_account = SavingAccount(450, 123456)

    def currency_open_account(self, num, bal):
        new_account = CurrencyAccount(450, 123456)


    def balance_show(self):
        return f"Customer {self.name}, Balance: {self.account.show_balance()}"

    def deposit_make(self, amount):
        self.account.deposit(amount)

    def withdraw_make(self, amount):
        self.account.withdraw(amount)

