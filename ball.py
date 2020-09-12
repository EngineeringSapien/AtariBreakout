import pygame
import random
from boundary import Boundary
import global_variables as gb


class Ball(Boundary):
	START_VELOCITY = (0,10)
	START_POSITION = (gb.width // 2, int(gb.height/9*6))
	
	def __init__(self, x, y, w, h, color, win):
		super().__init__(x, y, w, h, color, win)
		self.x_velocity = Ball.START_VELOCITY[0]
		self.y_velocity = Ball.START_VELOCITY[1]
		self.radius = int(gb.width/200)

	def draw(self):
		pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)

	def bounce_x(self):
		self.x_velocity = -self.x_velocity

	def bounce_y(self):
		self.y_velocity = -self.y_velocity

	def move_ball(self):
		self.x += self.x_velocity
		self.y += self.y_velocity

	def reset_ball(self):
		self.x = Ball.START_POSITION[0]
		self.y = Ball.START_POSITION[1]
		self.x_velocity = Ball.START_VELOCITY[0]
		self.y_velocity = Ball.START_VELOCITY[1]