import pygame
from boundary import Boundary
import global_variables as gb


class Paddle(Boundary):
	START_POSITION = (gb.width//2, int(gb.height/9*8))
	START_SIZE = (gb.width//8,gb.height//100)


	def __init__(self, x, y, w, h, color, win):
		super().__init__(x, y, w, h, color, win)
		self.speed = 10


	def move_left(self):
		self.x -= self.speed

	def move_right(self):
		self.x += self.speed

	# def reset_paddle(self):
	# 	self.x = 2







# p1 = Paddle(400,400,40,10,(250,250,250),WIN)
	