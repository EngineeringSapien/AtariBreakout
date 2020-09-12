import pygame
from boundary import Boundary


class Block(Boundary):
	total_blocks = 0
	blocks = []
	WIDTH = 60
	HEIGHT = 20

	def __init__(self, x, y, w, h, color, win):
		super().__init__(x, y, w, h, color, win)
		self.increase_blocks()
		self.w = Block.WIDTH
		self.h = Block.HEIGHT

	def increase_blocks(self):
		Block.total_blocks += 1
		Block.blocks.append(self)

	def collide(self):
		Block.blocks.pop(Block.blocks.index(self))
		Block.total_blocks -= 1
