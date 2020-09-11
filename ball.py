import pygame
import random
from boundary import Boundary
import global_variables as gb


class Ball(Boundary):
	START_VELOCITY = (0,10)
	START_POSITION = (gb.width // 2, int(gb.height/9*6)) #+ gb.height//50)

	def __init__(self, x, y, w, h, color, win):
		super().__init__(x, y, w, h, color, win)
		self.x_velocity = Ball.START_VELOCITY[0]
		self.y_velocity = Ball.START_VELOCITY[1]
		self.radius = int(gb.width/150)

	def draw(self):
		pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)

	def bounce_x(self):
		self.x_velocity = -self.x_velocity

	def bounce_y(self):
		self.y_velocity = -self.y_velocity
		# print("Y VELO: " + str(self.y_velocity))
		# pygame.time.delay(1000)

	def move_ball(self):
		self.x += self.x_velocity
		self.y += self.y_velocity

	def reset_ball(self): # get rid of these arguments
		self.x = Ball.START_POSITION[0]
		self.y = Ball.START_POSITION[1]
		self.x_velocity = Ball.START_VELOCITY[0]
		self.y_velocity = Ball.START_VELOCITY[1]


# b1 = Ball(300,300, 0, 0, (255, 255, 255), WIN)

# while True:
# 	WIN.fill((0,0,0))

# 	for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				quit()
		
# 	keys = pygame.key.get_pressed()
	# if keys[pygame.K_SPACE]:
		# b1.x_velocity = random.randint(-2,2)

# 	if b1.y > HEIGHT or b1.y < 0:
# 		b1.bounce_y()
# 	if b1.x > WIDTH or b1.x < 0:
# 		b1.bounce_x()

# 	b1.draw()
# 	b1.move_ball()

# 	pygame.display.update()