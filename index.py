import pygame
from pygame import mixer
import Pantallas
import NaveAnimacion
import Menu
import video
import nivel1
import random
import player
import xbox360_controller
import NaveLevel2 # Esto es level 2

# WILD SPACE
pygame.init()

pygame.mixer.music.load('Assets/sound/city.mp3')
pygame.mixer.music.set_volume(.2)
pygame.mixer.music.play(-1)

pantalla_x = 1152
pantalla_y = 640

nivel1bool = True

color_1 = (255, 1, 5)

size = (pantalla_x,pantalla_y)
level = 3
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None,50) ##
fontmini = pygame.font.Font(None,30) ##
screen_rect = screen.get_rect() ##
pygame.display.set_caption("WILD SPACE") ### MMMM

background = pygame.image.load("Assets/BF.jpg").convert()
background2 = pygame.image.load("Assets/BG_Nivel2.png").convert()
backgroundCave1 = pygame.image.load("Assets/BGCueva1.png").convert()
menu1 = pygame.image.load("Assets/menu0_2.jpg")
menu0 = pygame.image.load("Assets/menu0.jpg")


Nivel1 = nivel1.Nivel1(screen)
Pantalla1 = Pantallas.pantallaUno(screen)
Pantalla2 = Pantallas.pantallaDos(screen)
intrucciones3 = Pantallas.Intrucciones(screen)
Menu = Menu.background(screen)
PantallaCueva1 = Pantallas.pantallaCuevaUno(screen)
PantallaCueva2 = Pantallas.pantallaCuevaDos(screen)
pantallaMarte = Pantallas.pantallaMarte(screen)
# Pantalla1 = Pantallas.pantallaTres(screen)
LevelIntro = [False, False, False]
BackgroundAtomosfera = pygame.image.load("Assets/Level2/MarteAtmosfera.jpg").convert() # Level 2
animacionNave = NaveAnimacion.NaveBackground((64, 0))
NaveLevel = NaveLevel2.NaveLevel2((pantalla_x//2, pantalla_y//2+90))

# Esto es del level 2 --    
intro = NaveLevel2.Intro(screen)
cantidad = 9
enemylist = []
for x in range(cantidad):
    teorito = NaveLevel2.Teorito((random.randint(400,1452), (random.randint(20,80))*-1))
    enemylist.append(teorito)

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
    pygame.Rect(612, 560, 180, 5),
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

# Termina level 2 --
naveLand = False
patata = True
done = False
NuevoIntento = True ##
instruccionesPlataformer = True
musicPlataformer = False

Menu.Menu_entrada()
try:
    controller = xbox360_controller.Controller()
except:
    controller = None

clock = pygame.time.Clock()
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

patito = 0
lavaCollide = pygame.Rect(0, pantalla_y - patito, 1152, 640)

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
            if len(enemylist)>3:
              enemylist.pop()
            current_time = pygame.time.get_ticks() + 60000
            pygame.mixer.music.load('Assets/sound/final-voyage.mp3')
            pygame.mixer.music.play(1)
        current_time_2 = pygame.time.get_ticks()
        if current_time_2 >= current_time:
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
                #screen.blit(NaveLevel.image_explo, NaveLevel.rect_explo) ## WARNING
                #pygame.mixer.sound.load('Assets/sound/daño.mp3')
                #pygame.mixer.sound.play(1)
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
    if instruccionesPlataformer:
      intrucciones3.showIntro()
      instruccionesPlataformer = False
    if not musicPlataformer:
      pygame.mixer.music.load('Assets/sound/musicPlataformer1.mp3')
      pygame.mixer.music.play(-1)
      musicPlataformer = True
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

    if player.rect.y > 640:
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      musicPlataformer = False
      intrucciones3.showRestart()

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

    if oxigeno < 0:
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      musicPlataformer = False
      intrucciones3.showRestart()

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
      pygame.mixer.music.fadeout(3000)

    if oxigeno < 0 or player.rect.y > 490:
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      musicPlataformer = False
      intrucciones3.showRestart()

  #Desde aqui va la lava
  if level == 9:
    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%5)==0 and sec!=0 and PantallaCueva2.lavaIsUp == True:
      PantallaCueva2.lavaCount += 0.1
      patito += 0.1
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva5(player.buttonPressed)
    player.handle_event(event, collidersLevel7, paredLeftCollider7, paredRightCollider7, segundoBoton)
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.buttonPressed == True and numberOfPops == 0:
      paredLeftCollider7.pop()
      numberOfPops += 1
      PantallaCueva2.lavaIsUp = True
      PantallaCueva1.lavaIsUp = True
      pygame.mixer.music.load('Assets/sound/musicPlataformer2.mp3')
      pygame.mixer.music.play(-1)

    if player.rect.x < 20:
      level = 10
      player.rect.x = 1072
      player.rect.y = 348
      paredRightCollider6.append(pygame.Rect(1125, 0, 5, 640))
      PantallaCueva2.lavaCount = 1
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    if player.rect.colliderect(lavaCollide):
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      musicPlataformer = False
      intrucciones3.showRestart()
      
  #Aqui la lava empieza a subir despues del boton
  if level == 10:
    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(arboles2, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    if (sec%5)==0 and sec!=0 and PantallaCueva2.lavaIsUp == True:
      PantallaCueva2.lavaCount += 0.1
      patito += 0.1
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36) - 120, 1152, 640)

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
      PantallaCueva2.lavaCount = 1
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    if oxigeno < 0 or player.rect.colliderect(lavaCollide):
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      paredRightCollider6.pop()
      musicPlataformer = False
      intrucciones3.showRestart()

  if level == 11:
    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(arboles1, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    if (sec%5)==0 and sec!=0 and PantallaCueva2.lavaIsUp == True:
      PantallaCueva2.lavaCount += 0.1
      patito += 0.1
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

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
      PantallaCueva2.lavaCount = 1
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    if oxigeno < 0 or player.rect.colliderect(lavaCollide):
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      paredRightCollider6.pop()
      paredRightCollider5.pop()
      paredLeftCollider5.pop()
      paredLeftCollider5.append(pygame.Rect(0, 0, 40, 100))
      musicPlataformer = False
      intrucciones3.showRestart()

  if level == 12:
    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%5)==0 and sec!=0 and PantallaCueva2.lavaIsUp == True:
      PantallaCueva2.lavaCount += 0.1
      patito += 0.1
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva2(player.buttonPressed)
    player.handle_event(event, collidersLevel4, paredLeftCollider4, paredRightCollider4, primerBoton)
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.x < 10:
      level = 13
      player.rect.x = 1102
      player.rect.y = 598
      PantallaCueva2.lavaCount = 1
      patito = 0
      lavaCollide = pygame.Rect(0, 680 - (patito*36), 1152, 640)

    if player.rect.colliderect(lavaCollide):
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      paredRightCollider6.pop()
      paredRightCollider5.pop()
      paredLeftCollider5.pop()
      paredLeftCollider5.append(pygame.Rect(0, 0, 40, 100))
      paredLeftCollider4.pop()
      paredLeftCollider4.insert(0, pygame.Rect(0, 0, 40, 100))
      musicPlataformer = False
      intrucciones3.showRestart()

  if level == 13:
    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%5)==0 and sec!=0 and PantallaCueva2.lavaIsUp == True:
      PantallaCueva1.lavaCount += 0.1
      patito += 0.1
      lavaCollide = pygame.Rect(0, 680 - (patito*36), 1152, 640)

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva1.Cueva1()
    player.handle_event(event, collidersLevel3, paredLeftCollider3, paredRightCollider3, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.y < 20:
      level = 14
      player.rect.x = 80
      player.rect.y = 96
      patito = 0
      pygame.mixer.music.fadeout(3000)
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    if player.rect.colliderect(lavaCollide):
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      paredRightCollider6.pop()
      paredRightCollider5.pop()
      paredLeftCollider5.pop()
      paredLeftCollider5.append(pygame.Rect(0, 0, 40, 100))
      paredLeftCollider4.pop()
      paredLeftCollider4.insert(0, pygame.Rect(0, 0, 40, 100))
      musicPlataformer = False
      intrucciones3.showRestart()

  if level == 14:
    screen.blit(background, [0,0])

  pygame.display.flip()
  clock.tick(200)

pygame.quit
