import pygame

from spritesheet import SpriteSheet

import helpers

class Settings:
	"""
	Holds all settings of game.
	"""


	def __init__(self, bolan_game):
		"""
		Initialize Settings class.
		"""
		self.bolan_game = bolan_game

		# General settings
		self.screen_width = 1280
		self.screen_height = 600
		self.background_color = (255, 255, 255)
		self.display_caption = "Bolan.py"
		self.spritesheet_colorkey = (0, 0, 0)


		# Main menu settings 
		self.title_font = pygame.font.Font("fonts/PressStart2P.ttf", 48)
		self.title_image = self.title_font.render(
			"Bolan.py", True, (83, 83, 83))
		self.subtitle_font = pygame.font.Font("fonts/Fipps.otf", 16)
		self.subtitle_image = self.subtitle_font.render(
			"Press Space to Play", True, (83, 83, 83))


		# Bolan settings
		self.bolan_x_position = 20
		self.bolan_y_position = 440

		self.bolan_run_images = helpers.get_sprites(
			self.bolan_game, 2, 1854, 2, 88, 94)
		self.bolan_duck_images = helpers.get_sprites(
			self.bolan_game, 2, 2206, 6, 118, 94)
		self.bolan_standing_image = self.bolan_game.spritesheet.image_at(
			(1678, 2, 88, 94), colorkey=self.spritesheet_colorkey)
		
		self.bolan_update_rate = 60 # Update Bolan's image every 60 ticks.


		# Floor settings
		self.floor_rect = [2, 104, 2400, 26]
		self.floor_y = 500
		self.floor_speed = 1
		self.floor_image = self.bolan_game.spritesheet.image_at(
			self.floor_rect, self.spritesheet_colorkey)


		# Cactus settings
		self.cactus_y_position = 435

		self.cactus_small_images = helpers.get_sprites(
			self.bolan_game, 6, 443, 2, 35, 100,)
		self.cactus_big_images = helpers.get_sprites(
			self.bolan_game, 4, 652, 2, 50, 100)
		self.cactus_group_images = self.bolan_game.spritesheet.images_at([
			(481, 2, 68, 96), # Two small cacti.
			(549, 2, 102, 96), # Three small cacti.
			(802, 2, 150, 100), # Three big cacti, one small cactus.
			(702, 2, 100, 100), ], # Two big cacti.
			colorkey=self.spritesheet_colorkey,
		)

		self.cactus_images = (
			self.cactus_small_images + 
			self.cactus_big_images +
			self.cactus_group_images 
		)


		# Cloud settings
		self.cloud_image = self.bolan_game.spritesheet.image_at(
			(166, 2, 92, 27), colorkey=self.spritesheet_colorkey)
		self.cloud_x_range = range(100, 1180)
		self.cloud_y_range = range(75, 300)
		self.cloud_number = 6