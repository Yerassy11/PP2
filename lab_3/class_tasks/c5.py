class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Внесено: {amount}. Текущий баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Снято: {amount}. Текущий баланс: {self.balance}")

# Пример использования:
account = Account("Иван", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
