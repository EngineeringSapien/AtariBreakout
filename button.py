import pygame
from boundary import Boundary
from gui import TextGUI

class Button(Boundary):

	def __init__(self, x, y, w, h, color, win, text, font_size, destination=None):
		super().__init__(x, y, w, h, color, win)

		self.text = text
		self.font_size = font_size
		self.destination = destination

		self.button_text = TextGUI(self.x+self.w/4, self.y+self.h/4, self.win, self.text, self.font_size)

	def draw(self, cursor_x, cursor_y):
		if self.y + self.h > cursor_y > self.y and self.x + self.w > cursor_x > self.x:
			pygame.draw.rect(self.win, (0,0,255), (self.x, self.y, self.w, self.h))

			click = pygame.mouse.get_pressed()
			if click[0] == 1:
				self.destination()

		else:
			pygame.draw.rect(self.win, self.color, (self.x, self.y, self.w, self.h))
