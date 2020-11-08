import pygame

class NaveBackground():
    def __init__(self,position):
        self.sheet = pygame.image.load("Assets/BFR2.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = position
