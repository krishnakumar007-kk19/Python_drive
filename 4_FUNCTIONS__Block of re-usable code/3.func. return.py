
#Return is the keyword used to give back the result of a function within function
def sum(x,y):
    return x+y
print(sum(1,2))

sum1=sum(10,2)
print(sum1)

def perform_action(a,b):
    print(a*b)
perform_action(sum1,2)

#***************************************************************************************

#get value from user
#convert to lower case
#check i is there or not

def name():
    c=input("Enter the name: ")
    c=c.lower()
    return c
y=name()

def z(y):
    i=0
    count=0
    if i<len(y):
        y[i]=="i"
        i=i+1
        count=count+1
        print(i)
z(y)

#***************************************************************************************

#Assignment8.1
x=int()
def sqr(x):
    x=int(input("Enter the number: "))
    return x*x
print(sqr(x))

#***************************************************************************************

#Assignment8.2
x=int()
num=int()
def even(x):
    num=int(input("Enter the number: "))
    if num%2==0:
        print(num , "is even")
    else:
        print(num , "is odd")
    return num
print(even(x))

#***************************************************************************************
#Assignment8.3
w=""
z=int()
def string():
    w=input("Enter the word: ")
    z=len(w)
    return z
print(string())

#***************************************************************************************

#Assignment8.4
w=""
z=int()
def string():
    w=input("Enter the word: ")
    z=w[0]
    return z
print(string())

#***************************************************************************************