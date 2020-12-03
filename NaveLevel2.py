import pygame
import random

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

class NaveLevel2():
    def __init__(self,position):
        self.sheet = pygame.image.load("Assets/Level2/BFR2.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.vida = 100
        # bolitas de daño
        self.sheet_daño = pygame.image.load("Assets/Level2/warning.png")
        self.image_daño = self.sheet_daño.subsurface(self.sheet_daño.get_clip())
        self.rect_daño = self.image_daño.get_rect()
        self.rect_daño.center = position
        self.combiteclas = ['LEFT','RIGHT','UP','DOWN']
        self.combi = ['RIGHT','LEFT', 'DOWN','UP' ]
    
    def putPosition(self):
        random_y = random.randint(self.rect.y,self.rect.y+236)
        self.rect_daño.x += random.randint(-20, 20)
        self.rect_daño.y = random_y
        if len(self.combi) > 0:
            self.vida -= 15
        aux = []
        for x in range(4):
            aux.append(self.combiteclas[random.randint(0,3)])
        self.combi = aux

    def update(self, direccion):
        if self.rect.x > 0:
            if direccion == 'left':
                self.rect.x -=1
                self.rect_daño.x -=1

        if self.rect.x < 1152-113:
            if direccion == 'right':
                self.rect.x +=1
                self.rect_daño.x +=1
        
        if len(self.combi) != 0:
            if self.combi[-1] == 'LEFT': ## DEBE SER HEAD
                if direccion == 'LEFT':
                    if self.vida <= 95:
                        self.vida += 5
                    self.combi.pop() ## DEBE HACER POP
        if len(self.combi) != 0:
            if self.combi[-1] == 'RIGHT': ## DEBE SER HEAD
                if direccion == 'RIGHT':
                    if self.vida <= 95:
                        self.vida += 5
                    self.combi.pop() ## DEBE HACER POP
        if len(self.combi) != 0:
            if self.combi[-1] == 'UP': ## DEBE SER HEAD
                if direccion == 'UP':
                    if self.vida <= 95:
                        self.vida += 5
                    self.combi.pop() ## DEBE HACER POP
        if len(self.combi) != 0:
            if self.combi[-1] == 'DOWN': ## DEBE SER HEAD
                if direccion == 'DOWN':
                    if self.vida <= 95:
                        self.vida += 5
                    self.combi.pop() ## DEBE HACER POP


    def manejador_eventos(self, event):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.update('left')
        if keys[pygame.K_d]:
            self.update('right')
            
        if keys[pygame.K_LEFT]:
            self.update('LEFT')
        if keys[pygame.K_RIGHT]:
            self.update('RIGHT')
        if keys[pygame.K_UP]:
            self.update('UP')
        if keys[pygame.K_DOWN]:
            self.update('DOWN')

class Teorito():
  def __init__(self,position):
        self.sheet = pygame.image.load("Assets/Level2/teorito.png")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = position