class Student():
	""" This is a class example. The purpose of this class is to help beginners getting familiar of object oriented basics in python.The class illustrates a typical 'student'."""
	__studentId = 0
	__name = "Your name"
	__major = "Your major"

	def __init__(self, student_id, student_name, student_major):
		self.__studentId = student_id
		self.__name = student_name
		self.__major = student_major

	#setters
	def set_studentId(self, student_id):
		self.__studentId = student_id	

	def set_name(self, student_name):
		self.__name = student_name

	def set_major(self, student_major):
		self.__major = student_major

	#getters
	def get_studentId(self):
		return self.__studentId

	def get_name(self):
		return self.__name

	def get_major(self):
		return self.__major

	def __str__(self):
		return "The student's id is {student_id}, the name is {student_name} and major is {student_major}".format(student_id=self.__studentId, student_name=self.__name, student_major=self.__major)
#defining a subclass to the Student class
class Dorm(Student):
	__roomNumber = 0
	__electricityBill = 0
	__waterBill = 0

	def __init__(self, room_number, electricity_bill, water_bill, student_id, student_name, student_major):
		self.__roomNumber = room_number
		self.__electricityBill = electricity_bill
		self.__waterBill = water_bill
		Student.__init__(self, student_id, student_name, student_major)
	#setters
	def set_roomNumber(self, room_number):
		self.__roomNumber = room_number

	def set_electricityBill(self, electricity_bill):
		self.__electricityBill = electricity_bill

	def set_waterBill(self, water_bill):
		self.__waterBill = water_bill
	#getters
	def get_roomNumber(self):
		return self.__roomNumber

	def get_electricityBill(self):
		return self.__electricityBill

	def get_waterBill(self):
		return self.__waterBill
	# the print object function
	def __str__(self):
		return "The Dorm number is {dorm_number}. The dorm's electricity bill is {electricity_bill} RMB and the water bill is {water_bill} RMB. The student's id is {student_id}, student's name is {student_name} and student's major is {student_major}".format(dorm_number=self.__roomNumber, electricity_bill=self.__electricityBill, water_bill=self.__waterBill, student_id=Student.get_studentId(self), student_name=Student.get_name(self), student_major=Student.get_major(self))

student1 = Student('PC124', 'Chris', 'programming language')
print(student1)

dorm1 = Dorm(703, 200, 100, 'PC124', 'Chris', 'programming language')

print(dorm1)


