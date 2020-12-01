import pygame
from pygame import mixer
import Pantallas
import NaveAnimacion
import Menu
import video
import nivel1
import random
import xbox360_controller
from pygame import movie

pygame.init()

pygame.mixer.music.load('Assets/sound/city.mp3')
#pygame.mixer.music.play(-1)
pantalla_x = 1152
pantalla_y = 640

nivel1bool = True

color_1 = (255, 1, 5)

size = (pantalla_x,pantalla_y)
level = 1
screen = pygame.display.set_mode(size)

background = pygame.image.load("Assets/BF.jpg").convert()
background2 = pygame.image.load("Assets/BG_Nivel2.png").convert()

Nivel1 = nivel1.Nivel1(screen)
Pantalla1 = Pantallas.pantallaUno(screen)
Pantalla2 = Pantallas.pantallaDos(screen)
Menu = Menu.background(screen)
# Pantalla1 = Pantallas.pantallaTres(screen)
animacionNave = NaveAnimacion.NaveBackground((64, 0))
LevelIntro = [False, False, False]

naveLand = False
done = False

#Menu.Menu_entrada()
try:
    controller = xbox360_controller.Controller()
except:
    controller = None

while not done:
  posx, posy = pygame.mouse.get_pos()
  #print(f"x:{posx} y:{posy}")

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      if 498<posx<650 and 273<posy<430:
        level += 1
        Menu.Menu_salida()
        pygame.mixer.music.fadeout(3000)
        pygame.time.delay(3000)
        video.video1(screen)
        pygame.time.delay(1000)
        pygame.mixer.music.fadeout(1000)
        pygame.time.delay(1000)
        Menu.ShowPrimerNivel()
        
  
  if level == 0:
    Menu.inicio()
  
  if level == 1:
    ##Version 2
    if(nivel1bool):
      time_terminar = pygame.time.get_ticks() + 60000
      nivel1bool = False

    time_actual = pygame.time.get_ticks()
    segundos = (time_actual-time_terminar)//-1000
    if(time_actual >= time_terminar):
      if (Nivel1.verificar()):
        level = 3
      else: 
        Nivel1 = nivel1.Nivel1(screen)
        nivel1bool= True
    if controller != None:
            x, y = controller.get_left_stick()
            Nivel1.moveConControl(x, y)
    Nivel1.nivel(segundos)
    Nivel1.eventManager(event)
     ##Version 1
    #Nivel1.nivel1()
    #level = 3
  if level == 3:
    ## 
    if LevelIntro[0] != True:
      Pantalla1.inicioLVL(background)
      LevelIntro[0]= True      
    Pantalla1.inicio()
    screen.blit(animacionNave.image, animacionNave.rect)
    if naveLand == False:
        animacionNave.rect.y += 1
        if animacionNave.rect.y >= pantalla_y-364:
            print("aterrizo")
            naveLand = True
  if level == 4:
    screen.blit(background2,[0,0])
    Pantalla2.Plataformer_Nivel2()
  if level == 5:
    pass
    # Pantalla3.inicio()
  pygame.display.flip()

pygame.quit
