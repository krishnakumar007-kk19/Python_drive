
#stores data as key:value pair
d1={"id":1,"name":"kk"}
d2={'id':1,"name":"kk"}
print(d1)
print(d2)

print(type(d1))

d3=dict(a='parrot',b='eagle',c='crow')
print(d3)
print(d3.get('a'))
print(d3['b'])

d3['a']="peacock"
print(d3)

#to remove
d3.pop('a')
print(d3)

#to add or to change
d3['d']="sparrow"
print(d3)




