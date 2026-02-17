
set1 = {1,2,3}
print(set1) #{1, 2, 3}
set2 = {}
print(set2) #{}

#**************************************************************
#set wonot allow duplication/ duplicate value
#will take first value, 2nd duplicate value will be omitted

set3 = {1,2,6,6,8,8,10,10,3,4,4}
set4 = set(set3)
print(set4) #{1, 2, 3, 4, 6, 8, 10}

set3.remove(3)
print(set3) #{1, 2, 4, 6, 8, 10}

#**************************************************************
set2 = {1,2,3,4,5}
set3 = {8,7,6,5}

set2.difference_update(set3)
print(set2) #{1, 2, 3, 4}

set3.difference_update(set2)
print(set3) #{8, 5, 6, 7}

#**************************************************************
setA = {1,2}
setB = {1,2,3}

print(setA.issubset(setB)) #True
print(setB.issubset(setA)) #False

setA.difference_update(setB)
print(setA) #()

setB.difference_update(setA)
print(setB) #{3}
#**************************************************************
setA = {1,2,3}
setB = {1,2}

print(setA.issubset(setB)) #False
print(setB.issubset(setA)) #True

setA.difference_update(setB)
print(setA) #{3}

setB.difference_update(setA)
print(setB) #{1, 2}
#**************************************************************
