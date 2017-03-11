#----creating a list----

list1 = []
list2 = [1,2,3,4]

#----creating a list from a tuple----

tuple12 = 1,2,3,4
list3 = list(tuple12)

#----accessing data in the list----

sample_list = ['mike', 'jane', 'kevin', 'james']

#using index
print(sample_list[1]) #this is jane

#starting from the last element in the list
print(sample_list[-1])

#using a range to access data(slicing method)
new_list = sample_list[0:3]
print(new_list)


#----working with lists----
  
#replacing list values
list1 = [1,2,3,4]
list1[3] = 10
print(list1) #result: [1,2,3,10]

#replacing a subset of list values with a tuple
list1 = [1,2,3,4]
tuple1 = 10, 11
list1[1:3] = tuple1
print(list1) #result: [1,10,11,4]

#deleting list values
new_list = [2,3,4]
del new_list[1]
print(new_list)

#deleting using a range
list5 = [1,5,6,7,8]
del list5[1:3]
print(list5)

#using the pop() function
list5 = [9,8,7,6,5,4]
list5.pop(1)
print(list5) #result : [9,7,6,5,4]

#adding values to the end of a list usind the append() function
list7 = [1.2, 3.4, 5.6]
list7.append(4.4)
print(list7) #result: [1.2, 3.4, 5.6, 4.4]

#adding a value at a specific location in a list using the insert()
#syntax : insert(index value before which to place the new value, the new value)
list8 = [2.3, 4, 5, 6.7]
list8.insert(1, 7.8)
print(list8) #result: [2.3, 7.8, 4, 5, 6.7]

#concatenating lists using the extend() function
list9 = [1,2,3]
list10 = [4,5,6]
list9.extend(list9) #result: [1,2,3,4,5,6]

#----handy lists functions----

#counting how many times a specific value appears within a list using the count()
list11 = [1,5,8,1,6,1,8]
list11.count(1) #result: 3

#sorting data using the sort()
# The sort() function changes the original list
# to keep the original list and produce a new sorted list use sorted() function instead
list12 = ['oranges', 'apples', 'pears', 'bananas']
list12.sort()
print(list12) #result: ['apples', 'bananas', 'oranges', 'pears']

#getting the index of the a value in a list using the index()
list13 = [1,2]
list13.index(2) #result: 1

#reversing values within a list using the reverse()
# the reverse() function changes the original data
list13.reverse()
print(list13)

#the reversed() function
#returns an iterated object, it can not be accessed directly
list12 = ['oranges', 'apples', 'pears', 'bananas']
fruits = reversed(list12)
for fruit in fruits:
	print("My favorite fruit is ", fruit)

#----Multidimensional lists----

#declaration
list14 = [[1,2,3], [4,5,6], [7,8,9]]

#referencing an individual data
print(list14[0][1]) #result: 2
print(list14[2][2]) #result: 9

#----creating a list using List Comprehensions----
   
#syntax: [expression for variable in list]
list15 = [1,2,3,4]
list16 = [x*2 for x in list15]
print(list16) #result: [2,4,6,8]

#using the upper function
list17 = ['oranges', 'apples', 'pears', 'bananas']
list18 = [fruit.upper() for fruit in list17]
print(list18) #result: ['ORANGES', 'APPLES', 'PEARS', 'BANANAS']

