import pygame
from pygame import mixer
import Pantallas
import NaveAnimacion
import Menu
import video
import nivel1
import random
import xbox360_controller
import NaveLevel2 # Esto es level 2

# WILD SPACE
pygame.init()

pygame.mixer.music.load('Assets/sound/city.mp3')
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1)

pantalla_x = 1152
pantalla_y = 640

nivel1bool = True

color_1 = (255, 1, 5)

size = (pantalla_x,pantalla_y)
level = 0
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None,50) ##
fontmini = pygame.font.Font(None,30) ##
screen_rect = screen.get_rect() ##
pygame.display.set_caption("WILD SPACE") ### MMMM

background = pygame.image.load("Assets/BF.jpg").convert()
background2 = pygame.image.load("Assets/BG_Nivel2.png").convert()

Nivel1 = nivel1.Nivel1(screen)
Pantalla1 = Pantallas.pantallaUno(screen)
Pantalla2 = Pantallas.pantallaDos(screen)
Menu = Menu.background(screen)
# Pantalla1 = Pantallas.pantallaTres(screen)
LevelIntro = [False, False, False]
BackgroundAtomosfera = pygame.image.load("Assets/Level2/MarteAtmosfera.jpg").convert() # Level 2
animacionNave = NaveAnimacion.NaveBackground((64, 0))
NaveLevel = NaveLevel2.NaveLevel2((pantalla_x//2, pantalla_y//2+90))

# Esto es del level 2 --    
intro = NaveLevel2.Intro(screen)
cantidad = 5
enemylist = []
for x in range(cantidad):
    teorito = NaveLevel2.Teorito((random.randint(400,1452), -50))
    enemylist.append(teorito)

# Termina level 2 --
naveLand = False
patata = True
done = False
NuevoIntento = True ##

Menu.Menu_entrada()
try:
    controller = xbox360_controller.Controller()
except:
    controller = None

clock = pygame.time.Clock()

while not done:
  posx, posy = pygame.mouse.get_pos()
  #print(f"x:{posx} y:{posy}")
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = event.pos
      if 498<posx<650 and 273<posy<430 and level==0:
        level += 1
        Menu.Menu_salida()
        pygame.mixer.music.fadeout(3000)
        pygame.time.delay(3000)
        video.video1(screen)
        pygame.time.delay(1000)
        pygame.mixer.music.fadeout(3000)
        pygame.time.delay(3000)

  if level == 0:
    Menu.inicio()
  
  if level == 1:
    ##Version 2
    if(nivel1bool):
      pygame.mixer.music.load('Assets/sound/mountains.mp3')
      pygame.mixer.music.play(1)
      Nivel1.ShowPrimerNivel()
      time_terminar = pygame.time.get_ticks() + 60000
      nivel1bool = False

    time_actual = pygame.time.get_ticks()
    segundos = (time_actual-time_terminar)//-1000
    if(time_actual >= time_terminar):
      if (Nivel1.verificar()):
        level = 2
        Nivel1.nivelSalida()
        video.video2(screen)
      else: 
        Nivel1.nivelSalida()
        Nivel1 = nivel1.Nivel1(screen)
        nivel1bool= True
        pygame.mixer.music.fadeout(3000)
        Nivel1.showRestart()
    if controller != None:
            x, y = controller.get_left_stick()
            Nivel1.moveConControl(x, y)
    Nivel1.verificar()
    Nivel1.nivel(segundos)
    Nivel1.eventManager(event)
     ##Version 1
    #Nivel1.nivel1()
    #level = 3
  if level == 2:  # Obviamente Level 2
        # que el tiempo inicie aqui
        NaveLevel.manejador_eventos(event) # Level 2
        if NuevoIntento:
            # quiero reiniciar el tiempo aqui
            intro.showIntro()
            pygame.mixer.music.fadeout(1000)
            pygame.time.delay(1000)
            NaveLevel.vida = 100
            NuevoIntento = False
            current_time = pygame.time.get_ticks() + 60000
        current_time_2 = pygame.time.get_ticks()
        if current_time_2 >= current_time:
            print('puto roger, la cago')
            level += 1
        screen.blit(BackgroundAtomosfera, [0, 0])
        segundos = (current_time_2-current_time)//-1000
        texto_final = font.render(str(segundos),True,(255,255,255))
        texto_final_rect = texto_final.get_rect()
        texto_final_rect.center = screen_rect.center
        texto_x = texto_final_rect[0]
        screen.blit(texto_final,[texto_x,10])

        texto_2= fontmini.render(str(NaveLevel.combi[::-1]),True,(255,255,255))
        screen.blit(texto_2,[20,pantalla_y-50])

        screen.blit(NaveLevel.image, NaveLevel.rect)
        screen.blit(NaveLevel.image_daño, NaveLevel.rect_daño) ## WARNING
        if (segundos%10)==0 and segundos!=0:
            if patata:
                NaveLevel.putPosition()
                patata = False
        else:
            patata = True
        NaveLevel2.barra_vida(screen, pantalla_x//2-150, pantalla_y-55, NaveLevel.vida)
        for x in enemylist:
            screen.blit(x.image,x.rect)
            x.rect.y +=2
            x.rect.x -=2
            if x.rect.y > 840:
                x.rect.y = -100
                x.rect.x = random.randint(400,1452)
            if NaveLevel.rect.colliderect(x.rect):
                x.rect.y = 650
                # screen.blit(NaveLevel.fireimage,NaveLevel.rect)
                NaveLevel.vida -= 10
        if NaveLevel.vida <= 0:
            screen.blit(BackgroundAtomosfera, [0, 0])
            texto_final = font.render("EL BFR FUE DESTRUIDO",True,(255,255,255))
            texto_final_rect = texto_final.get_rect()
            texto_final_rect.center = screen_rect.center
            texto_x = texto_final_rect[0]
            screen.blit(texto_final,[texto_x,10])
            NuevoIntento = True ## cambiar cuando este listo el boton
            intro.showRestart()
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
  clock.tick(200)

pygame.quit
