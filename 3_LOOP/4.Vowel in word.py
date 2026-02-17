name = input("Enter your name: ")
print(name.lower())

i=0
count=0

while i<len(name):
    if (name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o'  or name[i]=='u'):
        count=count+1
    i=i+1
print(count)
