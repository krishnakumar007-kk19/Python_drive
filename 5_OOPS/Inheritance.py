
#single level inheritance/single inheritance
#1 parent properties -> 1 child accures
"""
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

"""


#Assignment :11
# Create a parent class "Person" with attributes "name" and "age", display_info() function.
# Create a child class inheriting from Person with additional attribute "salary" and
# override the function in parent class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
class Salary(Person):
    def __init__(self,name ,age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self,name ,age, salary):
        super().display()
        self.salary = salary
        print(self.salary)
obj= Salary("John",50,100000)
obj.display(obj.name,obj.age,obj.salary)
