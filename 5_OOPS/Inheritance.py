
#single level inheritance/single inheritance
#1 parent properties -> 1 child accures

class Animal: #Parent class
    def __init__(self, type):
        self.type = type
    def text(self):
        print(self.type)
class Dog(Animal): #Child class
    def sound(self):
        print("Bow Bow")
        super().text() #super() : Keyword to denote property of parent class
obj = Dog("Animal Type") #object name = class name()
obj.sound()


