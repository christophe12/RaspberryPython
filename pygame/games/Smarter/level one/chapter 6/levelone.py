import pygame, sys
from pygame.locals import *

pygame.init()

from smarter import Smarter
from question import Question
from animation import Animation
from random import *

class LevelOne(Smarter, Question, Animation):
	questions = [] #holds a list of all the questions
	state = 0 #holds the index of the current viewing question
	started_level = False # determines if the game has started or not
	optionsList = [] #stores informations about the options
	user_score = 0 # holds the points of the user
	game_score_rect = None # holds the game score_rect obj
	user_score_rect = None # holds the user score rect obj
	

	
	def __init__(self):
		Question.__init__(self, 'questions.txt')
		self.questions = self.get_questions()
		Smarter.__init__(self)
		Animation.__init__(self, self.displaysurf)

	#setters
	def set_levelstarted(self, start_l):
		self.started_level = start_l
	def set_user_score(self):
		self.user_score += int(self.data[self.state]['score'])

	#getters
	def get_colors(self):
		colors = {
			'background_color' : self.background_color,
			'main_color' : self.main_color,
			'orange' : self.orange,
			'navy_blue' : self.navy_blue,
			'yellow' : self.yellow
		}
		return colors

	#--- custom functions ----
	def startLevel(self):
		self.displaysurf.fill(self.background_color)
		self.state = self.chooseQuestion()
		self.drawingQuestion(self.questions[self.state]['question'])
		self.drawingOptions([self.questions[self.state]['option1'], self.questions[self.state]['option2'], self.questions[self.state]['option3']])
		self.drawWinningScore()
		self.drawUserScore()

	def finished(self):
		""" This function checks is the level has ended. if yes it returns True """
		if len(self.seen) == len(self.data):
			return True

	def started(self):
		if self.started_level == True:
			return True
		else:
			return False


	#---- questions related functions------

	def drawingQuestion(self, textl):
		""" This function draws the question to the screen """
		fontObj = pygame.font.SysFont('verdana', 20)
		textSurfaceObj = fontObj.render(textl, True, self.main_color)
		textRectObj = textSurfaceObj.get_rect()
		self.question_rect_width = textRectObj.width + 20 # the width of the text plus 20. we want the rectangle's width around the question to be greater than the question's width
		self.question_rect_height = textRectObj.height + 20 # same with the height, we want the height of the rectangle to be geater than the question height.
		self.window_spacing = (self.window_width - self.question_rect_width) / 2 # calculates the space to leave between the main window and the rectangle around the question.
		self.question_rectangle = pygame.Rect(self.window_spacing, 50, self.question_rect_width, self.question_rect_height)
		pygame.draw.rect(self.displaysurf, self.main_color, self.question_rectangle, 2)
		self.displaysurf.blit(textSurfaceObj, ((self.question_rectangle.topleft[0] + 10), (self.question_rectangle.topleft[1] + 10)))

	def drawingOptions(self, options):
		""" This function draws the question's options to the screen. This function's parameter is a list."""
		current_height = 0 #this will helps to leave a space between the rectangles around the options.
		counter = 0
		shuffle(options) #randomly rearranging the question's options
		for option in options:
			fontObj = pygame.font.SysFont('verdana', 15)
			optionSurfaceObj = fontObj.render(option, True, self.yellow)
			optionRectObj = optionSurfaceObj.get_rect()
			textwidth = optionRectObj.width
			textheight = optionRectObj.height
			spacing_width = (self.question_rect_width - textwidth) / 2 #calculating the width to leave between the rectangle around the option and the text.
			spacing_height = (self.question_rect_height - textheight) / 2 #calculating the height to leave between the rectangle around the option and the text.
			if current_height == 0:
				option_rectangle = pygame.Rect(5, 200, self.question_rect_width, self.question_rect_height)
				if counter == 0:
					# the OPTIONLIST will hold the x  and y intervals, a rect object and the text inside the rectangle around the option text
					self.optionsList.append({'option1':
						{
						'x': (option_rectangle.topleft[0], option_rectangle.topright[0]),
						'y': (option_rectangle.topleft[1], option_rectangle.bottomleft[1]),
						'rectangle' : option_rectangle,
						'text' : option
						}
						})
					counter += 1
				pygame.draw.rect(self.displaysurf, self.main_color, option_rectangle, 1)
				self.displaysurf.blit(optionSurfaceObj, ((option_rectangle.topleft[0] + spacing_width), (option_rectangle.topleft[1] + spacing_height)))
				current_height = option_rectangle.bottomleft[1]
			else:
				current_height += 10
				option_rectangle = pygame.Rect(5, current_height, self.question_rect_width, self.question_rect_height)
				if counter == 1:
					self.optionsList.append({'option2':
						{
						'x': (option_rectangle.topleft[0], option_rectangle.topright[0]),
						'y': (option_rectangle.topleft[1], option_rectangle.bottomleft[1]),
						'rectangle' : option_rectangle,
						'text' : option
						}
						})
					counter += 1
				else:
					self.optionsList.append({'option3':
						{
						'x': (option_rectangle.topleft[0], option_rectangle.topright[0]),
						'y': (option_rectangle.topleft[1], option_rectangle.bottomleft[1]),
						'rectangle' : option_rectangle,
						'text' : option
						}
						})
					counter = 0
				# print option_rectangle
				pygame.draw.rect(self.displaysurf, self.main_color, option_rectangle, 1)
				self.displaysurf.blit(optionSurfaceObj, ((option_rectangle.topleft[0] + spacing_width), (option_rectangle.topleft[1] + spacing_height)))
				current_height = option_rectangle.bottomleft[1]

	def checkAnswer(self, user_answer):
		""" This function checks if the answer the user has clicked is right or wrong. if right it returns True otherwise False."""
		if (self.data[self.state]['right-answer'] == user_answer):
			return True
		else:
			return False

	def initiate_states(self):
		""" This function will instantiate all the variables to their initial states."""
		self.set_levelstarted(False)
		self.question_rect_width = None
		self.question_rect_height = None
		self.window_spacing = 0
		self.question_rectangle = None
		self.optionsList = []
		self.covered = False
		self.covered_box = None
		self.covered_text = None
		self.text_x = 0
		self.hold_size = None


	def nextQuestion(self):
		""" This function will call the next question"""
		self.initiate_states()

	def calculateQuestionsScore(self):
		""" This function will go through the list of questions and adds on the scores. The return value will be a string."""
		score = 0
		for item in self.data:
			score += int(item['score'])

		return str(score)

	def drawWinningScore(self):
		""" This function will draw the score(for passing the level)to the screen"""
		# Score text title
		scoreObj = pygame.font.SysFont('verdana', 18)
		scoreSurfaceObj = scoreObj.render('Score', True, self.main_color)
		score_text_rect = scoreSurfaceObj.get_rect()
		scorex = self.window_width - (score_text_rect.width + 30)
		scorey = self.window_height - 370
	    
	    # rectangle around the score number
		score_rect_x = scorex
		score_rect_y = scorey + score_text_rect.height + 5
		score_rect_width = score_text_rect.width + 20
		score_rect_height = score_text_rect.height + 10
		score_rect = pygame.Rect(score_rect_x, score_rect_y, score_rect_width, score_rect_height)
		self.game_score_rect = score_rect #passing the score_rect properties
	    # the score number inside the rectangle
		score_number = self.calculateQuestionsScore()
		score_number_obj = pygame.font.SysFont('verdana', 18)
		score_number_surface_obj = score_number_obj.render(score_number, True, self.main_color)
		score_number_rect = score_number_surface_obj.get_rect()
		spacing_width = (score_rect.width - score_number_rect.width) / 2
		spacing_height = (score_rect.height - score_number_rect.height) / 2
		score_number_x = score_rect.topleft[0] + spacing_width
		score_number_y = score_rect.topleft[1] + spacing_height
		self.displaysurf.blit(scoreSurfaceObj, (scorex, scorey))
		pygame.draw.rect(self.displaysurf, self.main_color, score_rect, 1)
		self.displaysurf.blit(score_number_surface_obj, (score_number_x, score_number_y))

	def removeScore(self):
		pygame.draw.rect(self.displaysurf, self.background_color, self.user_score_rect)
		pygame.display.update()

	def drawUserScore(self):
		""" This function will draw and update the userscore on the main window."""
		game_score_rect = self.game_score_rect
		user_score_rect_x = game_score_rect.topleft[0]
		user_score_rect_y = game_score_rect.bottomleft[1] + 15
		user_score_rect = pygame.Rect(user_score_rect_x, user_score_rect_y, game_score_rect.width, game_score_rect.height)
	    
		pygame.draw.rect(self.displaysurf, self.main_color, user_score_rect, 1)

		if self.user_score == 0:
			user_score = str(self.user_score)
			user_score_text_obj = pygame.font.SysFont('verdana', 18)
			user_score_text_surface_obj = user_score_text_obj.render(user_score, True, self.main_color)
			user_score_text_rect = user_score_text_surface_obj.get_rect()
			spacing_width = (user_score_rect.width - user_score_text_rect.width) / 2
			spacing_height = (user_score_rect.height - user_score_text_rect.height) / 2
			user_score_text_x = user_score_rect.topleft[0] + spacing_width
			user_score_text_y = user_score_rect.topleft[1] + spacing_height
			self.user_score_rect = pygame.Rect(user_score_text_x, user_score_text_y, user_score_text_rect.width, user_score_text_rect.height)
			self.displaysurf.blit(user_score_text_surface_obj, (user_score_text_x, user_score_text_y))
		else:
			self.removeScore()
			user_score = str(self.user_score)
			user_score_text_obj = pygame.font.SysFont('verdana', 18)
			user_score_text_surface_obj = user_score_text_obj.render(user_score, True, self.main_color)
			user_score_text_rect = user_score_text_surface_obj.get_rect()
			spacing_width = (user_score_rect.width - user_score_text_rect.width) / 2
			spacing_height = (user_score_rect.height - user_score_text_rect.height) / 2
			user_score_text_x = user_score_rect.topleft[0] + spacing_width
			user_score_text_y = user_score_rect.topleft[1] + spacing_height
			self.user_score_rect = pygame.Rect(user_score_text_x, user_score_text_y, user_score_text_rect.width, user_score_text_rect.height)
			self.displaysurf.blit(user_score_text_surface_obj, (user_score_text_x, user_score_text_y))
			pygame.display.update()

		

	


