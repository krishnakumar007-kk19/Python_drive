

""""
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

##WHILE LOOPS :  : if condition is telling in question

name = "umbrella"
#position in name
i=0
#n(vowels)
count=0

while i<len(name):
    if (name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o'  or name[i]=='u'):
        count=count+1


    if (name[i]=='a' or
            name[i]=='e' or
            name[i]=='i' or
            name[i]=='o' or
            name[i]=='u'):
        count=count+1

    i=i+1
print(count)


"""

#Assignment 5.1
name1 = input("Enter your name: ")
print(name1.lower())
print(name1.upper())

#Assignment 5.2
name = input("Enter your name: ")
print(name.lower())

i=0
count=0

while i<len(name):
    if (name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o'  or name[i]=='u'):
        count=count+1
    i=i+1
print(count)

