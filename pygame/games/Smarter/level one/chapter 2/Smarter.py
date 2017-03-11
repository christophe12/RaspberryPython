import pygame, sys
from pygame.locals import *
import random
from random import randrange

pygame.init() #initializing the pygame library

#---- Loading the questions from a the file ----
data = [] #holds a list of all the questions
dict_list = {} # holds a dictionary containing information of one question

# add the questions to the data list as a dictionary
def addQuestion(text):
	global data, dict_list
	answer = text.split(',')
	counter = 0
	for i in answer:
		if counter != (len(answer) - 1):
			textSeparator = i.split(':')
			dict_list[textSeparator[0]] = textSeparator[1]
			counter += 1
	data.append(dict_list)
	dict_list = {}

#getting the file length. This will return the number of lines in the text file
def file_len(file_name):
	with open(file_name) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

fileLength = file_len('questions.txt') #storing the length of the file

my_file = open('questions.txt', 'r+')

def makeList():
	for the_data in range(fileLength - 1):
		file_reader = my_file.readline()
		addQuestion(file_reader)

# creating the question's list
makeList()

# preparing the surface
WINDOWWIDTH = 600
WINDOWHEIGHT = 500
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #setting the main window size
pygame.display.set_caption('Smarter')

#storing colors to be used
BACKGROUNDCOLOR = (16, 78, 139)
WHITE = (255, 255, 255)
ORANGE = (255, 147, 51)
NAVYBLUE = (0, 0, 128)
YELLOW = (255, 221, 51)

#necessary variable constants

STARTED = False #controls the start of the game
STATE = 0 #stores the index of the first question
QUESTIONRECTWIDTH = None #holds the width of the Rectangle around the question
QUESTIONRECTHEIGHT = None # holds the height of the Rectangle around the question
WINDOWSPACING = 0 # determines the space to leave between the rectangle around the question and the main window
QUESTIONRECTANGLE = None #stores the drawn rectangle object around the question
OPTIONSLIST = [] #stores informations about the options
SEEN = [] # holds the index of the questions that has already been seen by the user

def drawingQuestion(textl):
	""" This function draws the question to the screen """
	global QUESTIONRECTWIDTH, QUESTIONRECTHEIGHT, QUESTIONRECTANGLE, WINDOWSPACING
	fontObj = pygame.font.SysFont('verdana', 20)
	textSurfaceObj = fontObj.render(textl, True, WHITE)
	textRectObj = textSurfaceObj.get_rect()
	QUESTIONRECTWIDTH = textRectObj.width + 20 # the width of the text plus 20. we want the rectangle's width around the question to be greater than the question's width
	QUESTIONRECTHEIGHT = textRectObj.height + 20 # same with the height, we want the height of the rectangle to be geater than the question height.
	WINDOWSPACING = (WINDOWWIDTH - QUESTIONRECTWIDTH) / 2 # calculates the space to leave between the main window and the rectangle around the question.
	QUESTIONRECTANGLE = pygame.Rect(WINDOWSPACING, 50, QUESTIONRECTWIDTH, QUESTIONRECTHEIGHT)
	pygame.draw.rect(DISPLAYSURF, WHITE, QUESTIONRECTANGLE, 2)
	DISPLAYSURF.blit(textSurfaceObj, ((QUESTIONRECTANGLE.topleft[0] + 10), (QUESTIONRECTANGLE.topleft[1] + 10)))

def drawingOptions(options):
	""" This function draws the question's options to the screen. This function's parameter is a list."""
	global QUESTIONRECTWIDTH, QUESTIONRECTHEIGHT, OPTIONSLIST
	current_height = 0 #this will helps to leave a space between the rectangles around the options.
	counter = 0
	random.shuffle(options) #randomly rearranging the question's options
	for option in options:
		fontObj = pygame.font.SysFont('verdana', 15)
		optionSurfaceObj = fontObj.render(option, True, YELLOW)
		optionRectObj = optionSurfaceObj.get_rect()
		textwidth = optionRectObj.width
		textheight = optionRectObj.height
		spacing_width = (QUESTIONRECTWIDTH - textwidth) / 2 #calculating the width to leave between the rectangle around the option and the text.
		spacing_height = (QUESTIONRECTHEIGHT - textheight) / 2 #calculating the height to leave between the rectangle around the option and the text.
		if current_height == 0:
			option_rectangle = pygame.Rect(5, 200, QUESTIONRECTWIDTH, QUESTIONRECTHEIGHT)
			if counter == 0:
				OPTIONSLIST.append({'option1':
					{
					'x': (option_rectangle.topleft[0], option_rectangle.topright[0]),
					'y': (option_rectangle.topleft[1], option_rectangle.bottomleft[1]),
					'rectangle' : option_rectangle,
					'text' : option
					}
					})
				counter += 1
			pygame.draw.rect(DISPLAYSURF, WHITE, option_rectangle, 1)
			DISPLAYSURF.blit(optionSurfaceObj, ((option_rectangle.topleft[0] + spacing_width), (option_rectangle.topleft[1] + spacing_height)))
			current_height = option_rectangle.bottomleft[1]
		else:
			current_height += 10
			option_rectangle = pygame.Rect(5, current_height, QUESTIONRECTWIDTH, QUESTIONRECTHEIGHT)
			if counter == 1:
				OPTIONSLIST.append({'option2':
					{
					'x': (option_rectangle.topleft[0], option_rectangle.topright[0]),
					'y': (option_rectangle.topleft[1], option_rectangle.bottomleft[1]),
					'rectangle' : option_rectangle,
					'text' : option
					}
					})
				counter += 1
			else:
				OPTIONSLIST.append({'option3':
					{
					'x': (option_rectangle.topleft[0], option_rectangle.topright[0]),
					'y': (option_rectangle.topleft[1], option_rectangle.bottomleft[1]),
					'rectangle' : option_rectangle,
					'text' : option
					}
					})
				counter = 0
			# print option_rectangle
			pygame.draw.rect(DISPLAYSURF, WHITE, option_rectangle, 1)
			DISPLAYSURF.blit(optionSurfaceObj, ((option_rectangle.topleft[0] + spacing_width), (option_rectangle.topleft[1] + spacing_height)))
			current_height = option_rectangle.bottomleft[1]

# ---- choosing the question from the list randomly---

def checkIndexExistence(index):
	"""This function checks which index has already be chosen. returns True if it has and False otherwise."""
	global SEEN
	check_existence = False
	for item in SEEN:
		if index == item:
			check_existence = True
			break

	return check_existence


def chooseQuestion():
	"""This function choose an index randomly from the list of questions, checks if it has not be chosen already. If not it stores the chosen index in the SEEN list."""
	global STATE, SEEN
	random_index = randrange(0, len(data)) #choosing the index starting from 0 up to the length of the list.
	while (checkIndexExistence(random_index) == True):
		random_index = randrange(0, len(data))
		
	SEEN.append(random_index) # storing the chosen index in the SEEN list.
	STATE = random_index #stores the chosen index in the STATE variable


#the game loop
while True:
	if STARTED == False:
		DISPLAYSURF.fill(BACKGROUNDCOLOR)
		chooseQuestion() # chooses the question randomly
		drawingQuestion(data[STATE]['question']) #drawing the question on the screen
		drawingOptions([data[STATE]['option1'], data[STATE]['option2'], data[STATE]['option3']]) #drawing the options on the screen
		STARTED = True
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()