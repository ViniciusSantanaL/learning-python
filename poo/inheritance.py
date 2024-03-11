class Animal:
    def __init__(self, name):
        self.__name = name

    def walk(self):
        print("I am walking")

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("Au Au")


dog = Dog(name="Rex")
turtle = Animal(name="Jhon")

class AccountBank:
    def __init__(self, balance) -> None:
        self.__balance = balance

    def deposit(self, value):
        if value > 0:
            self.__balance += value

    def withdraw(self, value):
        if self.__balance >= value > 0:
            self.__balance -= value

    def get_balance(self):
        return self.__balance


account = AccountBank(balance=100)
account.deposit(10)
print(account.get_balance())
