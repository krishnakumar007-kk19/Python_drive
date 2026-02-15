
"""
for val in range(start, stop +1,steps): statements

Start value begins from 0 as default
Steps - value at which-> the amount incrementing
default value is 1

Membership operator is used in loops, as for string handling:
In keyword is the membership operator
range(5) = range(0,5,1)


##FOR LOOPS : if limit is telling in question

for i in range(1,6,1):
    print(i)

for i in range(5):
    print(i)

for i in range(1,6,2):
    print(i)

for i in range(2,7,2):
    print(i)



name = "krishna"

for i in name:
    print(name)
#Will print name 7 times

#fetched the length of name
size = len(name)
print(size)
#got value 7

for i in range(size):
    print(name[i])
#index value of name is mentioned by i

"""

#Assignment 6.1:
for i in range(1,11,2):
    print(i)

#Assignment 6.2:
name = " "
while name != "exit":
    name = input("Enter the text, please enter exit to stop entering text : ")
    print(name)
if name == "exit":
    print("Loop is closed")
