# Tuples...they're like lists but you can't change them after you make them

tuple8 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#checking whether a tuple contains a value
if 7 in tuple8:
	print("This tuple has a 7!")

if 8 not in tuple8:
	print("This tuple does not have an 8")

#finding the Number of values in a Tuple
print(len(tuple8))

#finding the Minimum and Maximum values in a Tuple
print(min(tuple8))

print(max(tuple8))