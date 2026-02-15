#Abstraction = displaying the necessary data & hiding the unnecessary ones
#taking money in atm & balance reflect in bank
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #pass is using in as for print
    def display(self):
        pass
class Dog(Animal):
    def display(self):
        print("Bow Bow")
obj=Dog()
obj.display()


#using in scenarios where privacy is important
#Test 2
from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def display(self):
        pass
class Withdraw(ATM):
    def display(self):
        total = 1000
        balance = total-500
class checkbalance(ATM):
    def display(self):
        total = 1000
        balance = total-500
        print(balance)
w=checkbalance()
w.display()

"""


#Assignment 12.1 :
# Create an abstract class 'Payment" with abstract function "pay".
# Inherit class "UPI" from "Payment" and override 'pay' in it.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class Upi(Payment):
    def pay(self):
        total = 1000
        balance = total-700
        print(balance)
w=Upi()
w.pay()





