#In Selenium : the output need to be saved as screenshot/..
#no where the output data is getting saved like -> .txt/.csv/.xml/.bin

#Can open in 3 modes :
#read -> only view
#write -> new file is created
#append -> updating the existing file


# 1. Write to a file (creates or overwrites)
file = open("contacts.txt", "w") #"w" to create a new output data file
file.write("Name: Alice, Phone: 1234567890\n")
file.write("Name: Bob, Phone: 9876543210\n")
file.close()  # Important: close the file!

# 2. Read and display contacts
file = open("contacts.txt", "r") #"r" to read output data from file : wonot create any new files
print("Contact List:")
for line in file:
    print(line.strip())
file.close()

# 3. append to a file (creates or updates new value)
file = open("contacts.txt", "a")  #"a" to create a new output data file/Add input to already having file
file.write("Name: Charlie, Phone: 5551234567\n")
file.close()


