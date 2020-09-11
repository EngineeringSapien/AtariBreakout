import pygame


class Boundary:
	def __init__(self, x, y, w, h, color, win):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color
		self.win = win

	def get_location(self):
		return (self.x, self.y)

	def get_size(self):
		return (self.w, self.h)

	def draw(self):
		pygame.draw.rect(self.win, self.color, (self.x, self.y, self.w, self.h))
