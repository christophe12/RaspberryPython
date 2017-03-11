import pygame, sys
from pygame.locals import *

pygame.init()

class Smarter():
	"""This is the main class of the game. It contains the main window's properties and functions that are common to all levels."""
	window_width = 600
	window_height = 500
	displaysurf = None
	FPS = 40
	fpsClock = pygame.time.Clock()

	#colors
	background_color = (16, 78, 139)
	main_color = (255, 255, 255)
	orange = (255, 147, 51)
	navy_blue = (0, 0, 128)
	yellow = (255, 221, 51)

	def __init__(self):
		self.displaysurf = pygame.display.set_mode((self.window_width, self.window_height))
		pygame.display.set_caption('Smarter')

	#setters
	def set_windowWidth(self, window_w):
		self.window_width = window_w

	def set_windowHeight(self, window_h):
		self.window_height = window_h

	#getters
	def get_windowWidth(self):
		return self.window_width

	def get_windowHeight(self):
		return self.window_height

	def get_displaySurface(self):
		return self.displaysurf
