import pygame
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
	        self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		
		log_event("asteroid_split")
		split_angle = random.uniform(20,50)
		split_radius = self.radius - ASTEROID_MIN_RADIUS
		first_split = Asteroid(self.position.x, self.position.y, split_radius)
		first_split.velocity = self.velocity.rotate(split_angle) * 1.2
		second_split = Asteroid(self.position.x, self.position.y, split_radius)
		second_split.velocity = self.velocity.rotate((split_angle * -1)) * 1.2