import pygame

import itertools


class Bolan:
	"""Represents Bolan, the T-Rex that the player plays as."""
	

	def __init__(self, bolan_game):
		"""Initalize Bolan class attributes."""
		self.bolan_game = bolan_game
		
		self.index = 0

		self.counter = 0

		self.images = self.images()
		self.image = self.images[self.index]


	def images(self):
		"""Returns sprites of Bolan from spritesheet."""
		rects = list()
		x = 1854
		for i in range(2):
			rects.append([x, 2, 88, 94])
			x += 88
		return self.bolan_game.spritesheet.images_at(rects, (0, 0, 0))


	def update(self):
		"""Updates the image of Bolan."""

		self.counter += 1
		if self.counter == 60:
			self.counter = 0
			self.index += 1

		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]


	def blitme(self):
		"""Blit Bolan onto the screen."""
		self.bolan_game.screen.blit(self.image, (20, 430))


class Floor:
	"""Represents the desert floor that Bolan runs on."""


	def __init__(self, bolan_game):
		"""Initalize Floor class attributes."""
		self.bolan_game = bolan_game
		self.image = self.bolan_game.spritesheet.image_at(
			[2, 104, 2400, 26], (0, 0, 0))
		self.rect = self.image.get_rect()

		self.x_1 = 0
		self.y_1 = 500

		self.x_2 = self.rect.width
		self.y_2 = 500

		self.speed = 1


	def update(self):
		"""Updates the coordinates of the object."""
		self.x_1 -= self.speed
		self.x_2 -= self.speed
		if self.x_1 <= -self.rect.width:
			self.x_1 = self.rect.width
		if self.x_2 <= -self.rect.width:
			self.x_2 = self.rect.width


	def blitme(self):
		"""Blits the floor onto the screen."""
		self.bolan_game.screen.blit(self.image, (self.x_1, self.y_1))
		self.bolan_game.screen.blit(self.image, (self.x_2, self.y_2))