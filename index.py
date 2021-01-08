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
import colliders

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
collisionDetected = colliders.Colliders()

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
    if event.type == pygame.JOYBUTTONDOWN:
      if event.button == xbox360_controller.A and level==0:
        level += 1
        Menu.Menu_salida()
        pygame.mixer.music.fadeout(3000)
        pygame.time.delay(3000)
        video.video1(screen)
        pygame.time.delay(1000)
        pygame.mixer.music.fadeout(3000)
        pygame.time.delay(3000)
        
        
  #event = pygame.event.get()
  if controller != None:
    pressed = controller.get_buttons()
  if level == 0:
    Menu.inicio()
  
  if level == 1:
    ##Version 2
    if(nivel1bool):
      pygame.mixer.music.load('Assets/sound/mountains.mp3')
      pygame.mixer.music.set_volume(1)
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
        if controller != None:
            x, y = controller.get_left_stick()
            NaveLevel.moveConControl(x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.B], pressed[xbox360_controller.X], pressed[xbox360_controller.Y])
        if NuevoIntento:
            # quiero reiniciar el tiempo aqui
            pygame.mixer.music.fadeout(1000)
            pygame.time.delay(1000)
            pygame.mixer.music.load('Assets/sound/final-voyage.mp3')
            pygame.mixer.music.set_volume(.2)
            pygame.mixer.music.play(1)
            intro.showIntro()
            NaveLevel.vida = 100
            NuevoIntento = False
            if len(enemylist)>3:
              enemylist.pop()
            current_time = pygame.time.get_ticks() + 60000
        current_time_2 = pygame.time.get_ticks()
        if current_time_2 >= current_time:
            video.video3(screen)
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
      pygame.mixer.music.fadeout(3000)
      pygame.time.delay(1000)
      intrucciones3.showIntro()
      instruccionesPlataformer = False
    if not musicPlataformer:
      pygame.mixer.music.load('Assets/sound/musicPlataformer1.mp3')
      pygame.mixer.music.set_volume(.2)
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
          if controller != None:
            x, y = controller.get_left_stick()
            player.moveConControl(event, collisionDetected.collidersLivel1, [], [], [], x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
          else:
            player.handle_event(event, collisionDetected.collidersLivel1, [], [], [])
          screen.blit(player.image,player.rect)
          clock.tick(15)
          if player.rect.x > 1152:
            level = 4
            player.rect.x = 0
            player.rect.y = pantalla_y - 64 - 39

  if level == 4:
    screen.blit(background, [0,0])
    pantallaMarte.superficieMarteCueva()
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLivel2, collisionDetected.paredLeftCollider2, collisionDetected.paredRightCollider2, [], x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event, collisionDetected.collidersLivel2, collisionDetected.paredLeftCollider2, collisionDetected.paredRightCollider2, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.y > 640:
      level = 5
      player.rect.x = 120
      player.rect.y = 100

  if level == 5:
    screen.blit(backgroundCave1, [0,0])
    PantallaCueva1.Cueva1()
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLevel3, collisionDetected.paredLeftCollider3, collisionDetected.paredRightCollider3, [], x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event, collisionDetected.collidersLevel3, collisionDetected.paredLeftCollider3, collisionDetected.paredRightCollider3, [])
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
      pygame.mixer.music.fadeout(3000)
      intrucciones3.showRestart()

  if level == 6:

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva2(player.buttonPressed)
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLevel4, collisionDetected.paredLeftCollider4, collisionDetected.paredRightCollider4, collisionDetected.primerBoton, x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event,collisionDetected.collidersLevel4, collisionDetected.paredLeftCollider4, collisionDetected.paredRightCollider4, collisionDetected.primerBoton)
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.buttonPressed == True and collisionDetected.numberOfPops == 0:
      collisionDetected.paredLeftCollider4.pop()
      collisionDetected.numberOfPops += 1
    if player.rect.x < 10:
      level = 7
      player.rect.x = 80
      player.rect.y = 96
      player.buttonPressed = False
      collisionDetected.numberOfPops = 0

  if level == 7:
    if isLevelOx:
      inicial_time = pygame.time.get_ticks() + 60000
      isLevelOx = False

    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(collisionDetected.arboles1, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva3()
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLevel5, collisionDetected.paredLeftCollider5, collisionDetected.paredRightCollider5, [], x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event, collisionDetected.collidersLevel5, collisionDetected.paredLeftCollider5, collisionDetected.paredRightCollider5, [])
    
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
      collisionDetected.paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      musicPlataformer = False
      pygame.mixer.music.fadeout(3000)
      intrucciones3.showRestart()

  if level == 8:

    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(collisionDetected.arboles2, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva4()
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLevel6, collisionDetected.paredLeftCollider6, collisionDetected.paredRightCollider6, [], x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event, collisionDetected.collidersLevel6, collisionDetected.paredLeftCollider6, collisionDetected.paredRightCollider6, [])
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
      collisionDetected.paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      musicPlataformer = False
      pygame.mixer.music.fadeout(3000)
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
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLevel7, collisionDetected.paredLeftCollider7, collisionDetected.paredRightCollider7, collisionDetected.segundoBoton, x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event, collisionDetected.collidersLevel7, collisionDetected.paredLeftCollider7, collisionDetected.paredRightCollider7, collisionDetected.segundoBoton)
    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.buttonPressed == True and collisionDetected.numberOfPops == 0:
      collisionDetected.paredLeftCollider7.pop()
      collisionDetected.numberOfPops += 1
      PantallaCueva2.lavaIsUp = True
      PantallaCueva1.lavaIsUp = True
      pygame.mixer.music.load('Assets/sound/musicPlataformer2.mp3')
      pygame.mixer.music.set_volume(.2)
      pygame.mixer.music.play(-1)

    if player.rect.x < 20:
      level = 10
      player.rect.x = 1072
      player.rect.y = 348
      collisionDetected.paredRightCollider6.append(pygame.Rect(1125, 0, 5, 640))
      PantallaCueva2.lavaCount = 1
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    if player.rect.colliderect(lavaCollide):
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      collisionDetected.paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      collisionDetected.paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      collisionDetected.numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      musicPlataformer = False
      pygame.mixer.music.fadeout(3000)
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)
      intrucciones3.showRestart()
      
  #Aqui la lava empieza a subir despues del boton
  if level == 10:
    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(collisionDetected.arboles2, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    if (sec%5)==0 and sec!=0 and PantallaCueva2.lavaIsUp == True:
      PantallaCueva2.lavaCount += 0.1
      patito += 0.1
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36) - 120, 1152, 640)

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva4()
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLevel6, collisionDetected.paredLeftCollider6, collisionDetected.paredRightCollider6, [], x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event, collisionDetected.collidersLevel6, collisionDetected.paredLeftCollider6, collisionDetected.paredRightCollider6, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    barra_vida(screen, 0, 0, oxigeno)

    if player.rect.x < 20:
      level = 11
      player.rect.x = 1072
      player.rect.y = 525
      collisionDetected.paredRightCollider5.append(pygame.Rect(1125, 0, 5, 640))
      collisionDetected.paredLeftCollider5.pop()
      collisionDetected.paredLeftCollider5.append(pygame.Rect(0, 136, 40, 504))
      PantallaCueva2.lavaCount = 1
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    if oxigeno < 0 or player.rect.colliderect(lavaCollide):
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      collisionDetected.paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      collisionDetected.paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      collisionDetected.numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)
      collisionDetected.paredRightCollider6.pop()
      musicPlataformer = False
      pygame.mixer.music.fadeout(3000)
      intrucciones3.showRestart()

  if level == 11:
    tiempo_ahora = pygame.time.get_ticks()
    sec = (tiempo_ahora-inicial_time)//-1000

    if (sec%2)==0 and sec!=0:
      if player.breath_air(collisionDetected.arboles1, oxigeno):
        oxigeno += 1
      else:
        oxigeno -= 1

    if (sec%5)==0 and sec!=0 and PantallaCueva2.lavaIsUp == True:
      PantallaCueva2.lavaCount += 0.1
      patito += 0.1
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    screen.blit(backgroundCave1, [0,0])
    PantallaCueva2.Cueva3()
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLevel5, collisionDetected.paredLeftCollider5, collisionDetected.paredRightCollider5, [], x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event, collisionDetected.collidersLevel5, collisionDetected.paredLeftCollider5, collisionDetected.paredRightCollider5, [])
    screen.blit(player.image,player.rect)
    clock.tick(15)
    barra_vida(screen, 0, 0, oxigeno)
    if player.rect.x < 20:
      level = 12
      player.rect.x = 40
      player.rect.y = 525
      collisionDetected.paredLeftCollider4.pop(0)
      collisionDetected.paredLeftCollider4.append(pygame.Rect(0, 136, 40, 504))
      PantallaCueva2.lavaCount = 1
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    if oxigeno < 0 or player.rect.colliderect(lavaCollide):
      level = 3
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      collisionDetected.paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      collisionDetected.paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      collisionDetected.numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)
      collisionDetected.paredRightCollider6.pop()
      collisionDetected.paredRightCollider5.pop()
      collisionDetected.paredLeftCollider5.pop()
      collisionDetected.paredLeftCollider5.append(pygame.Rect(0, 0, 40, 100))
      musicPlataformer = False
      pygame.mixer.music.fadeout(3000)
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
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLevel4, collisionDetected.paredLeftCollider4, collisionDetected.paredRightCollider4, collisionDetected.primerBoton, x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event, collisionDetected.collidersLevel4, collisionDetected.paredLeftCollider4, collisionDetected.paredRightCollider4, collisionDetected.primerBoton)
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
      patito = 0
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      collisionDetected.paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      collisionDetected.paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      collisionDetected.numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      collisionDetected.paredRightCollider6.pop()
      collisionDetected.paredRightCollider5.pop()
      collisionDetected.paredLeftCollider5.pop()
      collisionDetected.paredLeftCollider5.append(pygame.Rect(0, 0, 40, 100))
      collisionDetected.paredLeftCollider4.pop()
      collisionDetected.paredLeftCollider4.insert(0, pygame.Rect(0, 0, 40, 100))
      musicPlataformer = False
      pygame.mixer.music.fadeout(3000)
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
    if controller != None:
      x, y = controller.get_left_stick()
      player.moveConControl(event, collisionDetected.collidersLevel3, collisionDetected.paredLeftCollider3, collisionDetected.paredRightCollider3, [], x, y, pressed[xbox360_controller.A], pressed[xbox360_controller.X])
    else:
      player.handle_event(event, collisionDetected.collidersLevel3, collisionDetected.paredLeftCollider3, collisionDetected.paredRightCollider3, [])

    screen.blit(player.image,player.rect)
    clock.tick(15)
    if player.rect.y < 20:
      PantallaCueva1.lavaCount = 1
      level = 14
      player.rect.x = 80
      player.rect.y = 96
      patito = 0
      pygame.mixer.music.fadeout(3000)
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)

    if player.rect.colliderect(lavaCollide):
      level = 3
      patito = 0
      PantallaCueva1.lavaCount = 1
      lavaCollide = pygame.Rect(0, pantalla_y - (patito*36), 1152, 640)
      player.rect.x = 0
      player.rect.y = pantalla_y - 64 - 39
      oxigeno = 100
      collisionDetected.paredLeftCollider4.append(pygame.Rect(72, 420, 5, 144))
      collisionDetected.paredLeftCollider7.append(pygame.Rect(0, 0, 40, 640))
      collisionDetected.numberOfPops = 0
      player.buttonPressed = False
      PantallaCueva2.lavaIsUp = False
      PantallaCueva1.lavaIsUp = False
      PantallaCueva2.lavaCount = 1
      collisionDetected.paredRightCollider6.pop()
      collisionDetected.paredRightCollider5.pop()
      collisionDetected.paredLeftCollider5.pop()
      collisionDetected.paredLeftCollider5.append(pygame.Rect(0, 0, 40, 100))
      collisionDetected.paredLeftCollider4.pop()
      collisionDetected.paredLeftCollider4.insert(0, pygame.Rect(0, 0, 40, 100))
      musicPlataformer = False
      pygame.mixer.music.fadeout(3000)
      intrucciones3.showRestart()

  if level == 14:
    pygame.mixer.music.fadeout(3000)
    pygame.time.delay(3000)
    pygame.mixer.music.load('Assets/sound/time.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(1)
    intro.showLibro1()
    intro.showLibro2()
    intro.showFelicidades()
    video.video4(screen)
    pygame.mixer.music.fadeout(7000)
    intro.showFin()
    done = True

  pygame.display.flip()
  clock.tick(200)

pygame.quit
