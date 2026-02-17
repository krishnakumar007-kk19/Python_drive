#stores data as key:value pair
d1={"id":1,"name":"kk"}
d2={'id':2,"name":"kk1"}
print(d1) #{'id': 1, 'name': 'kk'}
print(d2) #{'id': 2, 'name': 'kk1'}

print(type(d1)) #<class 'dict'>
#***************************************************************************

d3=dict(a='parrot',b='eagle',c='crow')
print(d3)
print(d3.get('a'))
print(d3['b'])

#to add or to change
d3['a']="peacock"
d3['d']="sparrow"
print(d3)

#to remove
d3.pop('a')
print(d3)
#***************************************************************************

#Assignment 7.3
student = {1:"ravi",2:"surya",3:"arya"}
print(student) #{1: 'ravi', 2: 'surya', 3: 'arya'}
