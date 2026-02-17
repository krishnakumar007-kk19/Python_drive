
"""
list1=["a","b","c"]
print(list1) #['a', 'b', 'c']
print(type(list1)) #<class 'list'>
#***********************************************************
#Position of element in list
#list=[0, 1, 2, 3,..... -2, -1)]

list2=["c","b","a"]
print(list2[0]) #c
print(list2[1]) #b
print(list2[2]) #a
print(list2[-1]) #a
print(list2[-2]) #b

#****************************************************
list3=[]
print(list3) #[]
print(len(list3)) #0

list3=[1, 2, 3]
print(list3) #[1, 2, 3]
print(len(list3)) #3

#****************************************************
list1=["a","b","c"]
list1[1]="d"
print(list1)  #['a', 'd', 'c']

#****************************************************
list3=["10.3","b","c"]
print(list3) #['10.3', 'b', 'c']
print(list3.index("b")) #1 is position of b

#****************************************************
#To sort list in Alphabetical order
#list.sort()


list1=["d","u","a","t"]
list1.sort()
print(list1) #['a', 'd', 't', 'u']

#****************************************************
#To reverse the list in alphabetical order

list1=["d","u","a","t"]
list1.sort(reverse=True)
print(list1) #['u', 't', 'd', 'a']

###############This is string########################
list1=["10.3","2","55","-1"]
list1.sort(reverse=True)
print(list1)


###############This is numerical######################
list1=[10.3,2,55]
list1.sort(reverse=True)
print(list1)

#****************************************************
#delete element in list
list1.pop(2)
print(list1)
"""

#****************************************************

#Assignment4.1
veg_list=["tomato","potato","lemon"]
print(veg_list) #['tomato', 'potato', 'lemon']

#Assignment4.2
veg_list.sort()
print(veg_list) #['lemon', 'potato', 'tomato']

veg_list.sort( reverse =True)
print(veg_list) #['tomato', 'potato', 'lemon']

#Assignment4.3
print(veg_list[2]) #lemon

