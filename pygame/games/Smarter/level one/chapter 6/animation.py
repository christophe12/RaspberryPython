import pygame, sys
from pygame.locals import *

from smarter import Smarter

class Animation(Smarter):
	""" This class will handle all the animations in the game. """
	main_surf = None # this will hold the surface on which to perform the animation
	text_x = 0 #holds the x value for the text being animated
	hold_size = None #holds  the size of the previous text displayed on the screen(this is for the success or failure text animation)
	covered = False #checks if there's a covered box
	covered_box = None # holds the rect obj of the covered box if there's
	covered_text = None #holds the text inside the box which is covered

	def __init__(self, main_s):
		self.main_surf = main_s

	#--- level one animations------

	#----hovering effect------

	def checkHoveredBox(self, coordinates, OPTIONSLIST):
		"""This functions checks which box is being hovered on. Checks the mouse position in the intervals of X and Ys on each rectangle around the option text. The parameter is a tuple (x, y) of the mouse position."""
		counter = 1
		result = (False, None)
		
		if (coordinates[0] >= OPTIONSLIST[0]['option1']['x'][0]) and (coordinates[0] <= OPTIONSLIST[0]['option1']['x'][1]):
			if (coordinates[1] >= OPTIONSLIST[0]['option1']['y'][0]) and (coordinates[1] <= OPTIONSLIST[0]['option1']['y'][1]):
				result = (True, OPTIONSLIST[0]['option1']['rectangle'], OPTIONSLIST[0]['option1']['text'])
		
		if (coordinates[0] >= OPTIONSLIST[1]['option2']['x'][0]) and (coordinates[0] <= OPTIONSLIST[1]['option2']['x'][1]):
			if (coordinates[1] >= OPTIONSLIST[1]['option2']['y'][0]) and (coordinates[1] <= OPTIONSLIST[1]['option2']['y'][1]):
				result = (True, OPTIONSLIST[1]['option2']['rectangle'], OPTIONSLIST[1]['option2']['text'])
				
		if (coordinates[0] >= OPTIONSLIST[2]['option3']['x'][0]) and (coordinates[0] <= OPTIONSLIST[2]['option3']['x'][1]):
			if (coordinates[1] >= OPTIONSLIST[2]['option3']['y'][0]) and (coordinates[1] <= OPTIONSLIST[2]['option3']['y'][1]):
				result = (True, OPTIONSLIST[2]['option3']['rectangle'], OPTIONSLIST[2]['option3']['text'])
				
		return result

	def drawCover(self, box):
		""" This functions highlites the option box being hovered on by drawing the same rectangle with a different color on top of the current rectangle. The box parameter is a rect obj."""
		pygame.draw.rect(self.main_surf, self.orange, box, 1)

	def unCover(self, box):
		"""This function will uncover the previously covered rectangle. The parameter is a rect obj."""
		pygame.draw.rect(self.main_surf, self.main_color, box, 1)

	#-----pass/fail text animation----

	def removeWrittenText(self, size, textx):
		""" This function removes any previously written text before writing the next text on the screen by drawing a rectangle with the same width and height on top of the text."""
		text_width = size[0]
		text_height = size[1]
		textrect = pygame.Rect(textx, 140, text_width, text_height)
		pygame.draw.rect(self.main_surf, self.background_color, textrect)

	def animateText(self, feedback):
		""" This function will animate the success or failure text. The parameter will be a string indicating if the user has succeeded or not."""
		hold_feedback = None
		#checks the keyword passed
		if feedback == "succeeded":
			hold_feedback = "Right!"
		else:
			hold_feedback = "Wrong!"

		while (self.text_x != 230):
			if self.hold_size == None:
				self.text_x += 5
				fontObj = pygame.font.SysFont('verdana', 25)
				textSurfaceObj = fontObj.render(hold_feedback, True, self.main_color)
				text = textSurfaceObj.get_rect()
				self.hold_size = (text.width, text.height)
				self.main_surf.blit(textSurfaceObj, (self.text_x, 140))
				pygame.display.update()
			else:
				self.removeWrittenText(self.hold_size, self.text_x)
				self.text_x += 5
				fontObj = pygame.font.SysFont('verdana', 25)
				textSurfaceObj = fontObj.render(hold_feedback, True, self.main_color)
				text = textSurfaceObj.get_rect()
				self.hold_size = (text.width, text.height)
				self.main_surf.blit(textSurfaceObj, (self.text_x, 140))
				pygame.display.update()


