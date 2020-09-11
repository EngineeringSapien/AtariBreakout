import pygame
import random
from block import Block
from ball import Ball
from paddle import Paddle
from boundary import Boundary
from gui import GUI, TextGUI
from button import Button
from colors import *
import global_variables as gb
from taunts import all_taunts

pygame.init()
pygame.font.init()


class Game:
	FPS=60
	WIDTH, HEIGHT = (gb.width, gb.height)
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("BREAKOUT")
	
	def __init__(self, rows):
		self.run = False
		self.menu = True
		self.rows = rows
		self.columns = int(Game.WIDTH/Block.WIDTH)
		self.score = 0
		self.lives = 5
		self.level = 1

		self.the_ball = Ball(Ball.START_POSITION[0],Ball.START_POSITION[1],0,0,white,Game.WIN)
		self.the_paddle = Paddle(Paddle.START_POSITION[0],Paddle.START_POSITION[1],Paddle.START_SIZE[0],Paddle.START_SIZE[1],white,Game.WIN)
		self.score_text = TextGUI(Game.WIDTH//30, Game.HEIGHT//60, Game.WIN, "SCORE: " + str(self.score), 20)
		self.lives_text = TextGUI(Game.WIDTH/6*5, Game.HEIGHT - Game.HEIGHT//12, Game.WIN, "LIVES: " + str(self.lives), 15)
		self.level_text = TextGUI(Game.WIDTH/6*5, Game.HEIGHT//60, Game.WIN, "LEVEL: " + str(self.level), 20)

	def break_block(self, a_block):
		a_block.collide()
		self.the_ball.bounce_y()
		self.increase_score()

	def create_blocks(self):
		for c in range(1, self.columns+1):
			for r in range(3, self.rows+3):
				this_x = c*Block.WIDTH-(Block.WIDTH)
				this_y = r*Block.HEIGHT
				Block(this_x,this_y,0,0,random.choice(block_colors),Game.WIN)
		
	def increase_score(self):
		self.score += 10
		self.score_text.create_text("SCORE: " + str(self.score))

	def change_lives(self, amount):
		self.lives += amount
		self.lives_text.create_text("LIVES: " + str(self.lives))

	def change_level(self, amount):
		self.level += amount
		self.level_text.create_text("LEVEL: " + str(self.level))

	def lost_level(self):
		pygame.time.delay(666)
		self.change_lives(-1)
		self.reset_level()

	def increase_rows(self, increment):
		self.rows += increment

	def beat_level(self):
		pygame.time.delay(2000)
		self.change_level(1)
		self.change_lives(1)
		self.increase_rows(2)
		self.create_blocks()
		self.reset_level()

	def play_game(self):
		self.menu = False
		self.run = True
		self.main()

	def quit_game(self):
		quit()

	def redraw_window(self):
		Game.WIN.fill(black)
		for b in Block.blocks:
			b.draw()
		self.the_paddle.draw()
		self.the_ball.draw()
		self.score_text.draw()
		self.lives_text.draw()
		self.level_text.draw()

	def reset_level(self):
		self.the_ball.reset_ball()
		self.the_paddle.x = Game.WIDTH/2-Game.WIDTH/10/2

	def reset_game(self):
		self.score = 0
		self.lives = 5
		self.level = 1
		self.level_text.create_text("LEVEL: " + str(self.level))
		self.score_text.create_text("SCORE: " + str(self.score))
		self.lives_text.create_text("LIVES: " + str(self.lives))
		self.rows = 1

	def you_lose(self):
		Game.WIN.fill(black)
		loser_text = TextGUI(Game.WIDTH//2-Game.WIDTH//8, Game.HEIGHT//2, Game.WIN, random.choice(all_taunts), 20)
		loser_text.draw()
		self.reset_game()
		pygame.display.update()
		pygame.time.delay(5000)
		self.main_menu()

	def you_win(self):
		loser_text = TextGUI(Game.WIDTH//2-Game.WIDTH//4, Game.HEIGHT//2, Game.WIN, "YOU WIN!!!", 50)
		loser_text.draw()
		self.reset_game()
		pygame.display.update()
		pygame.time.delay(3000)
		self.main_menu()


	def main(self):
		self.reset_game()
		self.reset_level()
		self.create_blocks()

		clock = pygame.time.Clock()

		while self.run:
			
			clock.tick(Game.FPS)

			self.redraw_window()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
	
			keys = pygame.key.get_pressed()
			if keys[pygame.K_a] and self.the_paddle.x > 0:
				self.the_paddle.move_left()
			if keys[pygame.K_d] and self.the_paddle.x < Game.WIDTH - self.the_paddle.w:
				self.the_paddle.move_right()
			if keys[pygame.K_SPACE]:
				self.the_ball.x_velocity = random.randint(-10,10)


			if  self.the_ball.y < 0:
				self.the_ball.bounce_y()
			if self.the_ball.x > Game.WIDTH or self.the_ball.x < 0:
				self.the_ball.bounce_x()


			if self.the_ball.y > Game.HEIGHT:
				self.lost_level()


			for block in Block.blocks:
				if self.the_ball.y + self.the_ball.radius > block.y and self.the_ball.y - self.the_ball.radius < block.y + block.h:
					if self.the_ball.x + self.the_ball.radius > block.x and self.the_ball.x - self.the_ball.radius < block.x + block.w:
						self.break_block(block)


			if self.the_ball.y + self.the_ball.radius > self.the_paddle.y and self.the_ball.y - self.the_ball.radius < self.the_paddle.y + self.the_paddle.h:
				if self.the_ball.x + self.the_ball.radius > self.the_paddle.x and self.the_ball.x - self.the_ball.radius < self.the_paddle.x + self.the_paddle.w:

					if self.the_ball.x < self.the_paddle.x + self.the_paddle.w /2:
						normalized_ball_x = (self.the_ball.x - self.the_paddle.x)*-1
					elif self.the_ball.x >= self.the_paddle.x + self.the_paddle.w/2:
						normalized_ball_x = abs(self.the_ball.x - self.the_paddle.x - self.the_paddle.w)
					else:
						normalized_ball_x = (self.the_ball.x - self.the_paddle.x)*-1

					contact_point_fraction = (normalized_ball_x / self.the_paddle.w) + .0001
					regularized_fraction = int(1/contact_point_fraction/2)
					self.the_ball.x_velocity += regularized_fraction

					self.the_ball.bounce_y()


			if Block.blocks == []:
				if self.level == 8:
					self.run = False
					self.menu = True
					self.you_win()
				else:
					self.beat_level()


			if self.lives == 0:
				self.run = False
				self.menu = True
				self.you_lose()


			self.the_ball.move_ball()

			pygame.display.update()


	def main_menu(self):

		button_width = int(Game.WIDTH/6)
		button_height = int(Game.HEIGHT/10)

		title = TextGUI(Game.WIDTH//2-Game.WIDTH//10*2, Game.HEIGHT//3, Game.WIN, "BREAKOUT", Game.WIDTH//20)
		play_button = Button(int(Game.WIDTH/6*2 - button_width/2), int(Game.HEIGHT/3*2 - button_height), button_width, button_height, 
			random.choice([purple, orange]), Game.WIN, "PLAY", Game.WIDTH//60, self.play_game)

		quit_button = Button(int(Game.WIDTH/6*4 - button_width/2), int(Game.HEIGHT/3*2 - button_height), button_width, button_height,
			red, Game.WIN, "QUIT", Game.WIDTH//60, self.quit_game)

		clock = pygame.time.Clock()

		while self.menu:
			clock.tick(Game.FPS)

			Game.WIN.fill(black)

			Mouse_x, Mouse_y = pygame.mouse.get_pos()

			title.draw()

			play_button.draw(Mouse_x, Mouse_y)
			play_button.button_text.draw()

			quit_button.draw(Mouse_x, Mouse_y)
			quit_button.button_text.draw()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()

			pygame.display.update()


game1 = Game(1)
game1.main_menu()

