# Tuple declarations and assignments
tuple0 = () #empty tuple
tuple3 = 1,
tuple1 = (1,2,3,5)

# Accessing tuples
 # 1. using index
   print(tuple1[0])
   # result : 1

 # 2. using a range
   print(tuple1[1:3]) #notice that the first value to be printed is with index 1 but the last one is with index 2( 3 -1 )
   # result : (2, 3)
 # 3. using a range with a step amount
   tuple8 = 1,2,3,4,5,6,7,8,9,10
   tuple9 = tuple8[0:6:2]
   print(tuple9)
   #result : (1, 3, 5)

# concatenating tuples
  tuple3 = tuple3 + (4,)
  print(tuple3)
  # result : (1, 4)

# changing a tuple into a list
list1 = [4,5,6,7,8]
tuple4 = tuple(list1)
print(tuple4)




