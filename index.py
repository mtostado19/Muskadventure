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
    pygame.Rect(0, 576, 824, 20),
    pygame.Rect(1040, 576, 128, 20),
]
paredLeftCollider2 = [pygame.Rect(833, 576, 4, 60)]
paredRightCollider2 = [
  pygame.Rect(1023, 576, 8, 60),
  pygame.Rect(1152, 0, 10, 640)
  ]

collidersLevel3= [
    pygame.Rect(0, 160, 378, 5),
    pygame.Rect(228, 320, 360, 5),
    pygame.Rect(0, 440, 208, 5),
    pygame.Rect(324, 520, 180, 5),
    pygame.Rect(612, 480, 180, 5),
    pygame.Rect(828, 600, 360, 5),
    pygame.Rect(516, 240, 60, 20),
    pygame.Rect(0, 360, 60, 20),
    pygame.Rect(0, 80, 60, 20)
]
paredLeftCollider3 = [
  pygame.Rect(385, 170, 5, 36),
  ]
paredRightCollider3 = [
  pygame.Rect(576, 0, 36, 288),
  #pygame.Rect(228, 320, 5, 36),
  ]

collidersLevel4= [
    pygame.Rect(0, 565, 1152, 75),
    pygame.Rect(0, 136, 120, 36),
    pygame.Rect(230, 240, 150, 40),
    pygame.Rect(930, 240, 160, 40),
    pygame.Rect(230, 440, 160, 40),
    pygame.Rect(930, 440, 160, 40),
    pygame.Rect(510, 360, 280, 40),
]
paredLeftCollider4 = [
    pygame.Rect(0, 0, 40, 100),
    pygame.Rect(76, 172, 36, 252),
    pygame.Rect(72, 420, 5, 144),
    #pygame.Rect(0, 0, 40, 100),
]
paredRightCollider4 = [pygame.Rect(1116, 0, 5, 640)]

collidersLevel5= [
    pygame.Rect(0, 565, 1152, 75),
    pygame.Rect(0, 136, 155, 10),
    pygame.Rect(280, 200, 460, 10),
    pygame.Rect(910, 240, 490, 10),
    pygame.Rect(840, 320, 490, 10),
    pygame.Rect(770, 400, 490, 10),
    pygame.Rect(700, 480, 490, 10),
]
paredLeftCollider5 = [
    pygame.Rect(156, 136, 5, 10),
    pygame.Rect(0, 0, 40, 100),
]
paredRightCollider5 = [pygame.Rect(1116, 0, 5, 496)]

collidersLevel6= [
  pygame.Rect(0, 136, 156, 5),
  pygame.Rect(300, 220, 20, 5),
  pygame.Rect(440, 162.5, 20, 5),
  pygame.Rect(580, 220, 20, 5),
  pygame.Rect(790, 277.5, 20, 5),
  pygame.Rect(930, 335, 20, 5),
  pygame.Rect(1002, 388, 156, 5),
]
paredLeftCollider6 = [
  pygame.Rect(321, 220, 5, 420),
  pygame.Rect(461, 162.5, 5, 477.5),
  pygame.Rect(601, 220, 5, 420),
  pygame.Rect(811, 277.5, 5, 362.5),
  pygame.Rect(951, 355, 5, 285),
]
paredRightCollider6 = [
  pygame.Rect(279, 220, 5, 420),
  pygame.Rect(419, 162.5, 5, 477.5),
  pygame.Rect(559, 220, 5, 420),
  pygame.Rect(769, 277.5, 5, 362.5),
  pygame.Rect(909, 335, 5, 285),
]

collidersLevel7= [
  pygame.Rect(0, 352, 108, 10),
  pygame.Rect(108, 424, 144, 10),
  pygame.Rect(252, 388, 432, 10),
  pygame.Rect(684, 424, 144, 10),
  pygame.Rect(828, 496, 288, 10),
]
paredLeftCollider7 = [
  pygame.Rect(109, 352, 5, 72),
  pygame.Rect(686, 388, 5, 36),
  pygame.Rect(828, 424, 5, 144),
  pygame.Rect(0, 0, 40, 640),
]
paredRightCollider7 = [
  pygame.Rect(250, 388, 1, 36),
  pygame.Rect(1116, 0, 5, 640),
]

primerBoton = [pygame.Rect(600, 335, 80, 25)]
segundoBoton = [pygame.Rect(520, 367, 80, 25)]
numberOfPops = 0

clock = pygame.time.Clock()

naveLand = False
isLevelOx = False
done = False
oxigeno = 100
sec = 0
tiempo_ahora = 0
inicial_time = 0

arboles1 = [
  pygame.Rect(0, 397, 260, 168), 
  pygame.Rect(910, 102, 220, 140),
  pygame.Rect(1050, 453, 102, 27)
  ]

arboles2 = [
  pygame.Rect(280, 193, 40, 27),
  pygame.Rect(560, 193, 40, 27),
  pygame.Rect(910, 308, 40, 27),
]

def barra_vida(screen, x, y, vida):
        largo = 500
        ancho = 25
        calculo_barra = int((vida/100) * largo)
        borde = pygame.Rect(x, y, largo, ancho)
        rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
        pygame.draw.rect(screen, (255, 255, 255), borde, 3)
        if vida >= 60:
            pygame.draw.rect(screen, (85, 100, 235), rectangulo)
        else:
            pygame.draw.rect(screen, (255, 255, 40), rectangulo)
        if vida <= 30:
            pygame.draw.rect(screen, (185, 50, 40), rectangulo)

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
          player.handle_event(event, collidersLivel1, [], [], [])
          screen.blit(player.image,player.rect)
          clock.tick(15)
          if player.rect.x > 1152:
            level = 4
            player.rect.x = 0
            player.rect.y = pantalla_y - 64 - 39

  if level == 4:
    screen.blit(background, [0,0])
    pantallaMarte.superficieMarteCueva()
    player.handle_event(event, collidersLivel2, paredLeftCollider2, paredRightCollider2, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.y > 640:
      level = 5
      player.rect.x = 120
      player.rect.y = 100

  if level == 5:
    screen.blit(backgroundCave1, [0,0])
    PantallaCueva1.Cueva1()
    player.handle_event(event, collidersLevel3, paredLeftCollider3, paredRightCollider3, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.x > 1152:
      level = 6
      player.rect.x = 80
      player.rect.y = 96

  if level == 6:

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva2(player.buttonPressed)
    player.handle_event(event, collidersLevel4, paredLeftCollider4, paredRightCollider4, primerBoton)
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.buttonPressed == True and numberOfPops == 0:
      paredLeftCollider4.pop()
      numberOfPops += 1
    if player.rect.x < 10:
      level = 7
      player.rect.x = 80
      player.rect.y = 96
      player.buttonPressed = False
      numberOfPops = 0

  if level == 7:
    if isLevelOx:
      inicial_time = pygame.time.get_ticks() + 60000
      isLevelOx = False

    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(arboles1, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva3()
    player.handle_event(event, collidersLevel5, paredLeftCollider5, paredRightCollider5, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    barra_vida(screen, 0, 0, oxigeno)
    if player.rect.x > 1152:
      level = 8
      player.rect.x = 80
      player.rect.y = 96

  if level == 8:

    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(arboles2, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva4()
    player.handle_event(event, collidersLevel6, paredLeftCollider6, paredRightCollider6, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    barra_vida(screen, 0, 0, oxigeno)

    if player.rect.x > 1152:
      level = 9
      player.rect.x = 80
      player.rect.y = 312
      oxigeno = 100
    
  if level == 9:
    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva5(player.buttonPressed)
    player.handle_event(event, collidersLevel7, paredLeftCollider7, paredRightCollider7, segundoBoton)
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.buttonPressed == True and numberOfPops == 0:
      paredLeftCollider7.pop()
      numberOfPops += 1

    if player.rect.x < 20:
      level = 10
      player.rect.x = 1072
      player.rect.y = 348
      paredRightCollider6.append(pygame.Rect(1125, 0, 5, 640))


  #A partir de aqui el nivel sube
  if level == 10:
    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(arboles2, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva4()
    player.handle_event(event, collidersLevel6, paredLeftCollider6, paredRightCollider6, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    barra_vida(screen, 0, 0, oxigeno)

    if player.rect.x < 20:
      level = 11
      player.rect.x = 1072
      player.rect.y = 525
      paredRightCollider5.append(pygame.Rect(1125, 0, 5, 640))
      paredLeftCollider5.pop()
      paredLeftCollider5.append(pygame.Rect(0, 136, 40, 504))

  if level == 11:
    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(arboles1, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva3()
    player.handle_event(event, collidersLevel5, paredLeftCollider5, paredRightCollider5, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    barra_vida(screen, 0, 0, oxigeno)
    if player.rect.x < 20:
      level = 12
      player.rect.x = 40
      player.rect.y = 525
      paredLeftCollider4.pop(0)
      paredLeftCollider4.append(pygame.Rect(0, 136, 40, 504))

  if level == 12:
    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva2(player.buttonPressed)
    player.handle_event(event, collidersLevel4, paredLeftCollider4, paredRightCollider4, primerBoton)
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.x < 10:
      level = 13
      player.rect.x = 1112
      player.rect.y = 604

  if level == 13:
    screen.blit(backgroundCave1, [0,0])
    PantallaCueva1.Cueva1()
    player.handle_event(event, collidersLevel3, paredLeftCollider3, paredRightCollider3, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.y < 20:
      level = 14
      player.rect.x = 80
      player.rect.y = 96

  if level == 14:
    screen.blit(background, [0,0])

  pygame.display.flip()

pygame.quit
