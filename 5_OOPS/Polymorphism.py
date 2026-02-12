#polymorphism = ability to take more than 1 form = we use variable
#action is same, n(variables) changes -> example = sum (a,b) , sum(a,b,c)

#polymorphism types :
#1.function over-riding :


# using here 3 times display() function
#using in scenarios where privacy is important
#Test 2

class ATM(ABC):
    @abstractmethod
    def display(self):
    pass
class Withdraw(ATM):
    def display(self):
        total = 1000
        Balance = total-500
class checkbalance(ATM):
    def display(self):
        print(Balance)
w=Withdraw()
w.display()




#2.function over-loading : adding extra word+ input

#Qns :
#if an input is taken from user, print hello name. otherwise, print good morning

#Function over-loading
class Fruit:
    def display(self,name=None):
        if name:
            print("Hello" ,name)
        else:
            print("Bye")
obj=Fruit()
obj.display()
obj.display("mango")

