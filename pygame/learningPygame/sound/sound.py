import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((300, 200))
pygame.display.set_caption("how to play a sound in the background!")

#soundObj = pygame.mixer.Sound('sound.wav')
#soundObj.play()
#import time
#time.sleep(1) #wait and let the sound play for 1 second
#soundObj.stop()

#loading the music
pygame.mixer.music.load('instrumental.mp3')
pygame.mixer.music.play(-1, 0.0)

#pygame.mixer.music.stop() #stoping the background sound

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()

