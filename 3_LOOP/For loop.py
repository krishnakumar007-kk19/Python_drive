
"""
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
