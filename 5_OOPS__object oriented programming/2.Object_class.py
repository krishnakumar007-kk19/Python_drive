
#class -> collection of objects
#Class naming -> 1st letter should be capital letter

#Self -> to isolate objects & to distribute properties seperately
#constructor -> while creating a class,
#Abc school -> attribute
#x = property -> class/ global variables -> fixed input
#self.name / name = local / instance variable -> attribute in def
#display =
#Objects = Person
#properties = x, name

"""
class Person:
    x="ABC School"
    def __init__(self,name):   #this line is called constructor
        print("This is a constructor")
        self.name = name
    def display(self):
        print(self.name)
        print(Person.x)
person1=Person("Johns")
person1.display()
person2=Person("aby")
person2.display()



#Assignment 9.1
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
student1=Student("James",15)
student1.display()
student2=Student("John",14)
student2.display()

#Assignment 9.2:
class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    def display(self):
        print(self.title)
        print(self.pages)
book1=Book("The Tree",50)
book1.display()
book2=Book("The king",55)
book2.display()




"""
#Assignment 9.3: Create a class Person with a constructor that takes name and country
class Person:
    def __init__(self,name,country):
        self.name=name
        self.country=country
    def display(self):
        print(self.name)
        print(self.country)
person1=Person("James","England" )
person1.display()
person2= Person(input("What is Name : "),input("Country : ") )
person2.display()


