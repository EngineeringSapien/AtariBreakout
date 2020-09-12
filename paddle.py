import pygame
from boundary import Boundary
import global_variables as gb


class Paddle(Boundary):
	START_POSITION = (gb.width//2, int(gb.height/9*8))
	START_SIZE = (gb.width//12,gb.height//100)

	def __init__(self, x, y, w, h, color, win):
		super().__init__(x, y, w, h, color, win)
		self.speed = 10

	def move_left(self):
		self.x -= self.speed

	def move_right(self):
		self.x += self.speed
