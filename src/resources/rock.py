import pygame

class Rock:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.img = pygame.image.load("images/rock.png").convert_alpha()
		self.img = pygame.transform.smoothscale(self.img, (w, h))
		self.rect = self.img.get_rect()
		self.rect.center = (w / 2, h / 2)

	def draw():
		pass

	def load():
		pass
		
	def get_rect(self):
		return pygame.Rect(self.x, self.y, self.w, self.h)