#to store single set of data
#immutable

tuple1=()
print(tuple1) #()

tuple2=(3,50,30)
print(tuple2) #(3,50,30)

#***************************************************************************
#built-in function - tuple can be used on characters/alphabets only
#not on numeric
tuple3=tuple("abc")
print(tuple3) #('a', 'b', 'c')

x=(1,2,3,4)
print(tuple[x]) #tuple[1, 2, 3, 4]

list=[5,6,7,8,9]
tuple4 = tuple(list)
print(tuple4) #(5, 6, 7, 8, 9)

#***************************************************************************

tuple5=('a',)*3
print(tuple5) #('a', 'a', 'a')

#***************************************************************************
tuple2=(3,50,30)
print(tuple2[1]) #50

#sliced till 0,1
print(tuple2[:2]) #(3, 50)

#***************************************************************************
#then concatination happens
print(tuple2 + tuple3)

tuple1=(5,40,60)
tuple2=(3,50,30)
print(tuple1 + tuple2) #(5, 40, 60, 3, 50, 30)

#***************************************************************************

#Assignment 7.1
x=("x",)*5
print(x) #('x', 'x', 'x', 'x', 'x')

#Assignment 7.2
veg= ("cauliflower","onion","potato")
fruit= ("apple","banana","orange")
print(veg+fruit) #('cauliflower', 'onion', 'potato', 'apple', 'banana', 'orange')

