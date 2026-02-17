#n(parameters) can vary
#keyword = *args  -> it is a variable length func.
#* -> n(numbers)

#*****************************************************************************************
def sum(*args):
    s=0
    for i in args:
        s+=i
    return s
print(sum(2,3,4)) #9
print(sum(2,4,6,8,10)) #30
#*****************************************************************************************

def sub(*args):
    s=args[0]
    for i in args[1:]:
        s-=i
    print(s) #4
print(sub(10,2,2,2)) #None
#*****************************************************************************************

#1. Create a function that prints all arguments passed to it using *args
def word(*args):
    s=""
    for i in args:
        s+=i
    return s
print(word("Good"))
#*****************************************************************************************

#2. Write a function that multiplies all numbers passed using *args
def multiply(*args):
    s=1
    for i in args:
        s= s * i
    return s
print(multiply(1,3))


