######################## if_else #######################
if z>y:
    print(z)
else:
    print(y)

####################### if_elif #######################
if age<13:
    print("child")
elif age>=13 and age <=59:
    print("Adult")
else:
    print("old")

####################### for #######################
for i in range(1,11,2):      #range(start, stop +1,steps)
    print(i)

####################### while-if #######################
name = input("Enter your name: ")
print(name.lower())

i=0
count=0

while i<len(name):
    if (name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o'  or name[i]=='u'):
        count=count+1
    i=i+1
print(count)

