import pygame, sys
from pygame.locals import *

pygame.init()

from smarter import Smarter
from levelone import LevelOne

level_one = LevelOne()
Smarter = Smarter()

#game loop
while True:
	if level_one.started() == False:
		if not level_one.finished():
			level_one.startLevel()
			level_one.set_levelstarted(True)
		else:
			pygame.quit()
			sys.exit()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mouse = pygame.mouse.get_pos()
			result = level_one.checkHoveredBox(mouse, level_one.optionsList)
			if result[0]:
				if (level_one.covered == False) and (level_one.covered_box == None):
					level_one.drawCover(result[1]) #passing the rect obj for highliting the hovered option box
					level_one.covered_box = result[1]
					level_one.covered_text = result[2]
					level_one.covered = True
			else:
				if level_one.covered == True:
					level_one.unCover(level_one.covered_box)
					level_one.covered_box = None
					level_one.covered_text = None
					level_one.covered = False
		elif (event.type == MOUSEBUTTONUP) or (event.type == MOUSEBUTTONDOWN):
			mouse = pygame.mouse.get_pos()
			if level_one.covered:
				if level_one.checkAnswer(level_one.covered_text):
					level_one.animateText('succeeded')
					level_one.set_user_score()
					level_one.drawUserScore()
					pygame.time.delay(1000)
					level_one.nextQuestion()
				else:
					level_one.animateText('Failed')
					pygame.time.delay(1000)
					level_one.nextQuestion()


	pygame.display.update()
	Smarter.fpsClock.tick(Smarter.FPS)