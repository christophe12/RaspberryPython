#----creating a set----

set_name = set() #empty set

#----populating a set----

#syntax: set_name.add(element)

my_class = set()
my_class.add('Patience')
print(my_class)

#second option

my_class_2016 = set(['Yudis', 'Gupta', 'Mohammed'])
print(my_class_2016)

#----combining two sets to create a new set----

#The union() function

#if an element appears in the two sets. In the new set the element is added only once

my_class_2015 = set(['Mule', 'Abdoul', 'Ali'])

my_class_2015_2016 = my_class_2016.union(my_class_2015)

print(my_class_2015_2016) #result: {'Abdoul', 'Mule', 'Gupta', 'Yudis', 'Ali', 'Mohammed'}

#The intersection() function

my_class_2013 = set(['Yves', 'Bryan', 'Tanguy', 'Conrad'])
my_class_2014 = set(['Peace', 'Saga', 'Yves', 'Bryan'])

my_class_members_both_in_2013_and_2014 = my_class_2013.intersection(my_class_2014)

print(my_class_members_both_in_2013_and_2014) #result: {'Yves', 'Bryan'}

#the difference() function

my_class_members_in_2013_not_in_2014 = my_class_2013.difference(my_class_2014)

print(my_class_members_in_2013_not_in_2014) #result: {'Conrad', 'Tanguy'}

#the symmetric_difference() function

my_class_members_only_in_2013_and_in_2014 = my_class_2013.symmetric_difference(my_class_2014)

print(my_class_members_only_in_2013_and_in_2014) #result: {'Tanguy', 'Saga', 'Peace', 'Conrad'}

#----the update() function----

my_class_2016.update(['Hayder', 'Sam'])

print(my_class_2016) #result: {'Yudis', 'Gupta', 'Mohammed', 'Hayder', 'Sam'}

#----the remove() function and the discard() function----

#they both remove elements in a list but when the element doesn't exist the remove() throws an error, discrad() doesn't.

my_class_2016.remove('Sam')
print(my_class_2016)

my_class_2016.discard('Chris')
print(my_class_2016)