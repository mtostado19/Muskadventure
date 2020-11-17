import pygame
from pygame import mixer
import Pantallas
import NaveAnimacion
import NaveLevel2 # Esto es level 2
import random # Esto es level 2

# WILD SPACE
pygame.init()

pantalla_x = 1152
pantalla_y = 640

color_1 = (255, 1, 5)

size = (pantalla_x, pantalla_y)
level = 2
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None,50) ##
screen_rect = screen.get_rect() ##
pygame.display.set_caption("WILD SPACE") ### MMMM

background = pygame.image.load("Assets/BF.jpg").convert()
background2 = pygame.image.load("Assets/BG_Nivel2.png").convert()
BackgroundAtomosfera = pygame.image.load("Assets/Level2/MarteAtmosfera.jpg").convert() # Level 2

current_time = 0

Pantalla1 = Pantallas.pantallaUno(screen)
Pantalla2 = Pantallas.pantallaDos(screen)
animacionNave = NaveAnimacion.NaveBackground((64, 0))
NaveLevel = NaveLevel2.NaveLevel2((pantalla_x//2, pantalla_y//2+90))

# Esto es del level 2 --
def barra_vida(screen, x, y, vida):
    largo = 500
    ancho = 25
    calculo_barra = int((vida/100) * largo)
    borde = pygame.Rect(x, y, largo, ancho)
    rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
    pygame.draw.rect(screen, (255, 255, 255), borde, 3)
    if vida >= 60:
        pygame.draw.rect(screen, (50, 185, 40), rectangulo)
    else:
        pygame.draw.rect(screen, (255, 255, 40), rectangulo)
    if vida <= 30:
        pygame.draw.rect(screen, (185, 50, 40), rectangulo)
    

cantidad = 3
enemylist = []
for x in range(cantidad):
    teorito = NaveLevel2.Teorito((random.randint(400,1452), -50))
    enemylist.append(teorito)

# Termina level 2 --
naveLand = False
done = False
NuevoIntento = False ##

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    NaveLevel.manejador_eventos(event) # Level 2
    if level == 0:
        pass
    if level == 1:
        pass
    if level == 2:  # Obviamente Level 2
        if NuevoIntento:
            NaveLevel.vida = 100
            NuevoIntento = False
        current_time = 60 - pygame.time.get_ticks() //1000
        if current_time == 0:
            level += 1
        screen.blit(BackgroundAtomosfera, [0, 0])
        texto_final = font.render(str(current_time),True,(255,255,255))
        texto_final_rect = texto_final.get_rect()
        texto_final_rect.center = screen_rect.center
        texto_x = texto_final_rect[0]
        screen.blit(texto_final,[texto_x,10])
        screen.blit(NaveLevel.image, NaveLevel.rect)
        screen.blit(NaveLevel.image_daño, NaveLevel.rect_daño)
        barra_vida(screen, pantalla_x//2-250, pantalla_y-55, NaveLevel.vida)
        for x in enemylist:
            screen.blit(x.image,x.rect)
            x.rect.y +=1
            x.rect.x -=1
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
            NuevoIntento = False ## cambiar cuando este listo el boton
    if level == 3:
        screen.blit(background, [0, 0])
        Pantalla1.inicio()
        screen.blit(animacionNave.image, animacionNave.rect)
        if naveLand == False:
            animacionNave.rect.y += 1
            if animacionNave.rect.y >= pantalla_y-364:
                print("aterrizo")
                naveLand = True
    if level == 4:
        screen.blit(background2, [0, 0])
        Pantalla2.Plataformer_Nivel2()
    if level == 5:
        pass
    pygame.display.flip()

pygame.quit
