import pygame
from colors import *


pygame.font.init()
pygame.init()

class GUI:

	def __init__(self, x, y, win):
		self.x = x
		self.y = y
		self.win = win

	def draw(self, win):
		self.win.blit(self.thing)


class TextGUI(GUI):
	FONT_DIR = 'C:/Users/Avery/Projects/Breakout - PyGame/assets/fonts/AtariClassicExtrasmooth-LxZy.ttf'
	
	def __init__(self, x, y, win, text, font_size):
		super().__init__(x, y, win)
		self.text = text
		self.font_size = font_size
		self.font = pygame.font.Font('C:/Users/Avery/Projects/Breakout - PyGame/assets/fonts/AtariClassicExtrasmooth-LxZy.ttf', self.font_size)

		self.create_text(self.text)

	def create_text(self, new_text):
		text_surface = self.font.render(new_text, True, white)
		self.the_textSurface, self.the_textRec = text_surface, text_surface.get_rect()

	def draw(self):
		self.the_textRec = (self.x, self.y)
		self.win.blit(self.the_textSurface, self.the_textRec)
