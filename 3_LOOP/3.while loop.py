
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
