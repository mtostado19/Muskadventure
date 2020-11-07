import pygame
from pygame import mixer
import Pantallas

pygame.init()

pantalla_x = 1152
pantalla_y = 768

color_1 = (255, 1, 5)

size = (pantalla_x,pantalla_y)
level = 1
screen = pygame.display.set_mode(size)

background = pygame.image.load("Assets/BF.jpg").convert()

Pantalla1 = Pantallas.pantallaUno(screen)
# Pantalla2 = pantallas.pantallaDos(screen)
# Pantalla1 = pantallas.pantallaTres(screen)

done = False

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      x,y = event.pos
  screen.blit(background,[0,0])
  if level == 1:
    Pantalla1.inicio()
  if level == 2:
    pass
    # Pantalla2.inicio()
  if level == 3:
    pass
    # Pantalla3.inicio()
  pygame.display.flip()

pygame.quit