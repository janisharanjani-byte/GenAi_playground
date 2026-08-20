#DATA ABSTRACTION:
#it means DATA HIDING PROCESS
#it shows only the required functionalities by hiding the complexity of internal program ementation.
#to achieve abstraction in python, we use abc module .

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")

    def stop(self):
        print("Car stops using brakes")


car = Car()
car.start()
car.stop()


#DATA ENCAPSULATON
#it means DATA WRAPPING PROCESS
#Encapsulationencapsulation can be implemented using private variables (__).

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

account = BankAccount(5000)

account.deposit(2000)

print(account.get_balance())




















