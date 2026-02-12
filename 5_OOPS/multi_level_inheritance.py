
class Vehicle:
    def __init__(self,speed):
        self.speed=speed
    def display1(self):
        print(self.speed)
class Car(Vehicle):
    def __init__(self,speed,mileage):
        super().__init__(speed)
        self.mileage=mileage
    def display1(self):
        super().display1()
        print(self.mileage)
class Smartcar(Car):
    def __init__(self,speed,mileage,engine):
        super().__init__(speed,mileage)
        self.engine=engine
    def display1(self):
        super().display1() #Function over-riding
        print(self.engine)
Obj1=Smartcar(100,200,1000)
Obj1.display1()

#Function over-riding :- polymporphism concept that executes the functions of child class only
# when function name is same in both parent & child.

#Obj2=Smartcar(a,b,c)

a=input("enter speed: ")
b=input("enter mileage: ")
c=input("enter engine: ")
obj2=Smartcar(a,b,c)
obj2.display1()

#abstraction : display only necessary items, rest is neglected
