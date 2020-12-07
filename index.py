import pygame
from pygame import mixer
import Pantallas
import NaveAnimacion
import player


pygame.init()

#pygame.mixer.music.load('Assets/sound/city.mp3')
#pygame.mixer.music.play(-1)
pantalla_x = 1152
pantalla_y = 640

color_1 = (255, 1, 5)

size = (pantalla_x,pantalla_y)
level = 3
screen = pygame.display.set_mode(size)

background = pygame.image.load("Assets/BF.jpg").convert()
background2 = pygame.image.load("Assets/BG_Nivel2.png").convert()
backgroundCave1 = pygame.image.load("Assets/BGCueva1.png").convert()
menu1 = pygame.image.load("Assets/menu0_2.jpg")
menu0 = pygame.image.load("Assets/menu0.jpg")


Pantalla1 = Pantallas.pantallaUno(screen)
Pantalla2 = Pantallas.pantallaDos(screen)
PantallaCueva1 = Pantallas.pantallaCuevaUno(screen)
PantallaCueva2 = Pantallas.pantallaCuevaDos(screen)
pantallaMarte = Pantallas.pantallaMarte(screen)
# Pantalla1 = Pantallas.pantallaTres(screen)
animacionNave = NaveAnimacion.NaveBackground((64, 0))

player = player.Player((0, pantalla_y - 64 - 39))
collidersLivel1 = [pygame.Rect(0, 576, 1152, 64)]
collidersLivel2 = [
    pygame.Rect(0, 576, 824, 64),
    pygame.Rect(1040, 576, 128, 64),
]
paredLeftCollider2 = [pygame.Rect(833, 576, 4, 60)]
paredRightCollider2 = [pygame.Rect(1023, 576, 8, 60)]

collidersLevel3= [
    pygame.Rect(0, 160, 378, 5),
    pygame.Rect(228, 320, 360, 5),
    pygame.Rect(0, 440, 208, 5),
    pygame.Rect(324, 520, 180, 5),
    pygame.Rect(612, 480, 180, 5),
    pygame.Rect(828, 600, 360, 5),
]
paredLeftCollider3 = []
paredRightCollider3 = [pygame.Rect(576, 0, 36, 288)]

collidersLevel4= [
    pygame.Rect(0, 565, 1152, 75),
    pygame.Rect(0, 136, 120, 36),
    pygame.Rect(210, 240, 170, 40),
    pygame.Rect(910, 240, 170, 40),
    pygame.Rect(210, 440, 170, 40),
    pygame.Rect(910, 440, 170, 40),
    pygame.Rect(490, 360, 320, 40),
]
paredLeftCollider4 = [
    pygame.Rect(0, 0, 40, 100),
    pygame.Rect(76, 172, 36, 252),
]
paredRightCollider4 = []

collidersLevel5= [
    pygame.Rect(0, 565, 1152, 75),
    pygame.Rect(0, 136, 120, 36),
    pygame.Rect(210, 240, 170, 40),
    pygame.Rect(910, 240, 170, 40),
    pygame.Rect(210, 440, 170, 40),
    pygame.Rect(910, 440, 170, 40),
    pygame.Rect(490, 360, 320, 40),
]
paredLeftCollider5 = [
    pygame.Rect(0, 0, 40, 100),
    pygame.Rect(76, 172, 36, 252),
]
paredRightCollider5 = []

clock = pygame.time.Clock()

naveLand = False
done = False

while not done:
  posx, posy = pygame.mouse.get_pos()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      if 217 < posx < 333 and 150 < posy < 300:
        level += 1
        #pygame.mixer.music.stop()
      x,y = event.pos
  
  if level == 0:
    if 217 < posx < 333 and 150 < posy < 300:
      screen.blit(menu1,[0,0])
    else: 
      screen.blit(menu0,[0,0])

  if level == 1:
    screen.blit(background,[0,0])
    Pantalla1.inicio()
    screen.blit(animacionNave.image, animacionNave.rect)
    if naveLand == False:
        animacionNave.rect.y += 1
        if animacionNave.rect.y >= pantalla_y-364:
            print("aterrizo")
            naveLand = True
  if level == 2:

    screen.blit(background2,[0,0])
    Pantalla2.Plataformer_Nivel2()

  if level == 3:
    screen.blit(background, [0,0])
    pantallaMarte.superficieMarte()
    screen.blit(animacionNave.image, animacionNave.rect)
    if naveLand == False:
        animacionNave.rect.y += 1
        if animacionNave.rect.y >= pantalla_y-300:
            print("aterrizo")
            naveLand = True
    if naveLand == True:
          player.handle_event(event, collidersLivel1, [], [])
          screen.blit(player.image,player.rect)
          clock.tick(15)
          if player.rect.x > 1152:
            level = 4
            player.rect.x = 0
            player.rect.y = pantalla_y - 64 - 39

  if level == 4:
    screen.blit(background, [0,0])
    pantallaMarte.superficieMarteCueva()
    player.handle_event(event, collidersLivel2, paredLeftCollider2, paredRightCollider2)
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.y > 640:
      level = 5
      player.rect.x = 60
      player.rect.y = 0

  if level == 5:
    screen.blit(backgroundCave1, [0,0])
    PantallaCueva1.Cueva1()
    player.handle_event(event, collidersLevel3, paredLeftCollider3, paredRightCollider3)
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.x > 1152:
      level = 6
      player.rect.x = 80
      player.rect.y = 0

  if level == 6:
    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva2()
    player.handle_event(event, collidersLevel4, paredLeftCollider4, paredRightCollider4)
    screen.blit(player.image,player.rect)
    player.barra_vida(screen, 0, 0, 100)
    clock.tick(15)
    #if player.rect.x > 10:
      #level = 7
      #player.rect.x = 80
      #player.rect.y = 0

  if level == 7:
    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva3()

  pygame.display.flip()

pygame.quit
