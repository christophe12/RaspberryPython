from random import *

class Question():
	""" This class will deal with retrieving questions from the question file.(for all the levels)"""
	#attributes
	data = [] #this will hold the list of the questions retrieved from the question file
	seen = [] # holds the indecies of the questions that has already been seen by the user 

	def __init__(self, filename):
		self.makeList(filename)

	#getters
	def get_questions(self):
		return self.data

	def checkIndexExistence(self, index):
		"""This function checks which index has already be chosen. returns True if it has and False otherwise."""
		check_existence = False
		for item in self.seen:
			if index == item:
				check_existence = True
				break

		return check_existence

	def chooseQuestion(self):
		"""This function choose an index randomly from the list of questions, checks if it has not be chosen already. If not it stores the chosen index in the SEEN list."""
		random_index = randrange(0, len(self.data)) #choosing the index starting from 0 up to the length of the list.
		while (self.checkIndexExistence(random_index) == True):
			random_index = randrange(0, len(self.data))
			
		self.seen.append(random_index) # storing the chosen index in the SEEN list.
		level_state = random_index #stores the chosen index in the STATE variable
		return level_state


	# add the questions to the question list as a dictionary
	def addQuestion(self, text):
		dict_list = {}
		answer = text.split(',')
		counter = 0
		for i in answer:
			if counter != (len(answer) - 1):
				textSeparator = i.split(':')
				dict_list[textSeparator[0]] = textSeparator[1]
				counter += 1
		self.data.append(dict_list)

	#getting the file length. This will return the number of lines in the text file
	def file_len(self, file_name):
		with open(file_name) as f:
			for i, l in enumerate(f):
				pass
		return i + 1	

	def makeList(self, filename):
		fileLength = self.file_len(filename) #storing the length of the file
		my_file = open(filename, 'r+')
		for the_data in range(fileLength):
			file_reader = my_file.readline()
			self.addQuestion(file_reader)
