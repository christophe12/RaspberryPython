#----how to create a dictionary----

student = {} #empty dictionary

#----populating a dictionary----
	
#syntax : dictionary_name = {key1:value1, key2:value2...}
student = {'PC123':'Paul','PC124':'Jason','PC125':'Raz'}

#second option
student2 = {}
student2['PC123'] = 'Paul'

#----obtaining data from a dictionary----
	
#syntax ; dictionary_name[key]

print(student['PC124']) #result: Jason

#----the use of get() function----
   
#the get() function can help you to return a custom message if the value you asked for is not available
print(student.get('PC178', "We couldn't find the value you asked for!"))

#----getting the keys of a dictionary
print(student.keys())

#----changing values in a dictionary

student['PC123'] = "Paul Walker"
print(student['PC123']) #result: Paul Walker

#----deleting values in a dictionary

del student['PC125']
print(student) #result: {'PC123':'Paul','PC124':'Jason'}

#----handy functions---

# len(dictionary_name) -> Returns the number of elements in a dictionary

# dictionary_name.values() -> Returns the current values in the dictionary

# dictionary_name.items -> Returns a tuple that contains the dictionary's key/value pairs

# dictionary_name.clear() -> Removes all the dictionary's elements




