
#set wonot allow duplication/ duplicate value
#will take first value, 2nd duplicate value will be omitted


set1 = {1,2,3}
print(set1)
set2 = {}
print(set2)


set3 = {1,2,6,6,8,8,10,10,3,4,4}
set4 = set(set3)
print(set4)

set3.remove(3)
print(set3)

set2 = {1,2,3,4}
set3 = {8,7,6,5}

set2.difference_update(set3)
print(set2)

set3.difference_update(set2)
print(set3)




#setA = {1,2}
#setB = {1,2,3}

setA = {1,2,3}
setB = {1,2}

#setA.difference_update(setB)
#print(setA)

#setB.difference_update(setA)
#print(setB)

print(setA.issubset(setB))
print(setB.issubset(setA))


