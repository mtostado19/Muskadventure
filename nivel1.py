import pygame

class Nivel1():
  def __init__(self, screen):
    self.screen = screen
    self.pantalla_x = 1152
    self.pantalla_y = 640

    self.hud = pygame.image.load("Assets/HUDlvl1.png")
    self.hud_image = self.hud.subsurface(self.hud.get_clip())
    self.hud_rect = self.hud_image.get_rect()
 
  
  def nivel1(self):
    pygame.draw.rect(self.screen,(0,0,0) ,[0,0,self.pantalla_x, self.pantalla_y])
    self.screen.blit(self.hud,[self.pantalla_x//2-self.hud_rect.x, self.pantalla_y//2-self.hud_rect.y])
