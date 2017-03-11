# This program will give you 3 tries to put in the number 3...

right_number = 3
for y in range(1, 4):
	x = input("enter the number")
	if (int (x) == right_number):
		print("Congratulations!...you have given the right number")
		break
	else:
		print("wrong number, try again")