#access modifiers

#1.public = Any data/function from any class can be accessed
#2.private = A particular class only will get accessed, no elsewhere have access to that data/function
#3.protected = in case, inheritance -> only accessible in child subclass, can be accessed internally not outside

#should use getter function & setter function

#to get the data already in the loop: getter
#to update to latest input giving : setter

class Car:
    def __init__(self,name,mileage): # __init taken as private
        self.name = name # public access modifier is default access modifier
        self._mileage = mileage # _ is used as for protected access modifier
        self.__price = 200 # __ is used for private access modifier
    def get_price(self):
        return self.__price #return - as to reuse the value 
    def set_price(self,price):
        self.__price = price
obj1 = Car("ford",100)
obj1.set_price(1000)
print(obj1.get_price())


