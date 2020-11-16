import pygame

class NaveLevel2():
    def __init__(self,position):
        self.sheet = pygame.image.load("Assets/Level2/BFR3.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.vida = 100

    def update(self, direccion):
        if self.rect.x > 0:
            if direccion == 'left':
                self.rect.x -=1

        if self.rect.x < 1152-113:
            if direccion == 'right':
                self.rect.x +=1

    def manejador_eventos(self, event):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.update('left')
        if keys[pygame.K_d]:
            self.update('right')

class Teorito():
  def __init__(self,position):
        self.sheet = pygame.image.load("Assets/Level2/teorito.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = position