#----creating a string----

string1 = "This is a string"

#----long strings----

string2 = ''' This is a very very long 
string'''
print(string2)

#----retrieving a subset of a string----

# Retrieving a character

string3 = "I like python language"

print(string3[4]) #result: k

#using a range

print(string3[4:8]) #result: ke p

#----the partition() function----

string4 = string3.partition('li')
print(string4) #result: ('I', 'li', 'ke python language')

#----the replace() function----
#syntax: replace(old, new)
string5 = string3.replace('language', 'programming language')
print(string5) #result: I like python programming language

#----the split() function----

string6 = string5.split()
print(string6) #result: ['I', 'like', 'python', 'programming', 'language']

#----the joining() function----
string7 = ' '.join(string6)
print(string7) #result: I like python programming language

#----handy string testing functions----

#isalnum -> Returns True if the string contains only numbers and letters.
#isalpha() -> Returns true if the string caontains only letters.
#isdecimal -> Returns true is the string contains only decimal characters
#is digit() -> returns true if the string contains only numbers
#isidentifier() -> returns true if the string is a valid python
#islower() -> returns true if the string contains only lowercase characters.
#isnumeric() -> returns true if the string contains only numeric characters.
#isprintable() -> returns true if the string contains only printable characters.
#isspace() -> returns true if the string contains only whitespace characters.
#istitle() -> returns true if the string is in title format
#isupper() -> returns true if the string contains only uppercase characters.


#----the find() and rfind() functions---

string7 = "This is how we find a substring in a string"
#the find() function returns -1 when the substring is not found
print(string7.find('how')) #result: h

print(string7.find('how', 8, 13)) #the find() with a starting and ending index for the search

print(string7.rfind('string')) #the rfind() starts the search from the right side and throws an error if the substring is not found

#----the format() function----

#with positional placeholders

number1 = 5
number2 = 4
result = number1 + number2

print("The result of adding {0} and {1} is {2}".format(number1, number2, result))

#with named placeholders

fruit = 'apple'

print("My favorite fruit is {fav}".format(fav=fruit))