import pygame
import random

class Nivel1():
  def __init__(self, screen):
    self.screen = screen
    self.pantalla_x = 1152
    self.pantalla_y = 640

    self.hudGreen = pygame.image.load("Assets/HUDGreen.png")
    self.hudRed = pygame.image.load("Assets/HUDRed.png")

    self.naveOG = pygame.image.load("Assets/Nave.png")
    self.naveOG_x = 512
    self.naveOG_y = 1647

    self.refuelOG = pygame.image.load("Assets/refuel.png")
    self.refuelOG_x = 132
    self.refuelOG_y = 129
  
    self.porcentaje = .05
    self.naveX = 0
    self.naveY = 0

    self.nave = pygame.transform.scale(self.naveOG,(int(self.naveOG_x*self.porcentaje), int(self.naveOG_y*self.porcentaje)))
    self.nave_image = self.nave.subsurface(self.nave.get_clip())
    self.nave_rect = self.nave_image.get_rect()

    self.refuel = pygame.transform.scale(self.refuelOG,(int(self.refuelOG_x*self.porcentaje), int(self.refuelOG_y*self.porcentaje)))
    self.refuel_image = self.refuel.subsurface(self.refuel.get_clip())
    self.refuel_rect = self.refuel_image.get_rect()
    
    self.initX = 576 + random.randint(-320 + self.nave_rect[2], 320 - self.nave_rect[3])
    self.initY = 320 + random.randint(-315, 315)

    self.font = pygame.font.Font(None,40) ##
    self.done = True
    self.LastMovement = ''
    self.Alineado = False
    self.sOGx = 5
    self.sOGy = 10
    self.s = pygame.Surface((5,10), pygame.SRCALPHA)
    self.s_rect = self.s.get_rect()   # per-pixel alpha
    self.s_rect[3] = self.sOGx*self.porcentaje
    self.s_rect[2] = self.sOGy*self.porcentaje
    self.s.fill((255,255,255,255)) 
    
    
  def nivel(self, segundos):
    pygame.draw.rect(self.screen,(0,0,0) ,[0,0,self.pantalla_x, self.pantalla_y])   
    self.screen.blit(self.nave, [self.initX//2 - self.nave_rect[2]//2 + self.naveX, self.initY//2 - self.nave_rect[3]//2 + self.naveY])
    self.screen.blit(self.refuel, [self.initX//2 - self.nave_rect[2]//4 + self.naveX , self.initY//2 - (self.nave_rect[3]//14) + self.refuel_rect[3] +self.naveY])
    if (self.Alineado):
      self.screen.blit(self.hudGreen,[0,0])  
    else:
      self.screen.blit(self.hudRed,[0,0])

    ##self.screen.blit(self.s,[self.initX//2 - self.nave_rect[2]//4 + self.naveX + self.refuel_rect[2]//2 - self.s_rect[2]//2, self.initY//2 - (self.nave_rect[3]//14) + self.refuel_rect[3] +self.naveY + self.refuel_rect[3]//2 - self.s_rect[3]//2 - 2 ])
    #self.screen.blit(self.nave,[self.initX - self.nave_rect.x//2, self.initY - self.nave_rect.y//2])
    #self.screen.blit(self.refuel,[self.initX - self.nave_rect.x//2 - self.refuel_rect.x, self.initY - self.nave_rect.y//2 - self.refuel_rect.y])    
    
    
    self.porcentaje += .00009

    self.nave = pygame.transform.scale(self.naveOG,(int(self.naveOG_x*self.porcentaje), int(self.naveOG_y*self.porcentaje)))
    self.nave_image = self.nave.subsurface(self.nave.get_clip())
    self.nave_rect = self.nave_image.get_rect()

    self.refuel = pygame.transform.scale(self.refuelOG,(int(self.refuelOG_x*self.porcentaje), int(self.refuelOG_y*self.porcentaje)))
    self.refuel_image = self.refuel.subsurface(self.refuel.get_clip())
    self.refuel_rect = self.refuel_image.get_rect()
    self.update(self.LastMovement)

    self.s_rect[3] = int(self.sOGx*self.porcentaje)
    self.s_rect[2] = int(self.sOGy*self.porcentaje)

    texto_final = self.font.render("Segundos para el encuentro: " + str(segundos),True,(255,255,255))
    self.screen.blit(texto_final,[10,10])

  def update(self, direction):
    if direction == 'left':
        self.LastMovement = 'left'
        self.naveX += .070
    if direction == 'right':
        self.LastMovement = 'right'
        self.naveX -= .070

    if direction == 'up':
        self.LastMovement = 'up'
        self.naveY += .070
    if direction == 'down':
        self.LastMovement = 'down'
        self.naveY -= .070

    if direction == 'down-left':
        self.LastMovement = 'down-left'
        self.naveY -= .070
        self.naveX += .070
    if direction == 'down-right':
        self.LastMovement = 'down-right'
        self.naveY -= .070
        self.naveX -= .070

    if direction == 'up-right':
      self.LastMovement = 'up-right'
      self.naveY += .070
      self.naveX -= .070
    if direction == 'up-left':
      self.LastMovement = 'up-left'
      self.naveY += .070
      self.naveX += .070
    if direction == '':
      pass

  def eventManager(self, event):
    if event.type == pygame.QUIT:
        done = True

    if event.type == pygame.KEYDOWN:
        #print(event)
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.update('left')
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.update('right')

        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.update('up')
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.update('down')

        if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
            self.update('down-left')
        if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
            self.update('down-right')
        
        if (event.key == pygame.K_UP or event.key == pygame.K_w) and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
            self.update('up-left')
        if (event.key == pygame.K_UP or event.key == pygame.K_w) and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
            self.update('up-right')
            

        if event.key == pygame.K_SPACE:
            self.isJump = True
            self.music.saltar()
  
  def moveConControl(self, x, y):
    if y < 0 and x == 0:
        self.update('up')
    if y > 0 and x == 0:
        self.update('down')

    if x < 0 and y == 0:
        self.update('left')
    if x > 0 and y == 0:
        self.update('right')

    if  x > 0 and y < 0:
        self.update('up-right')
    if  x > 0 and y > 0:
        self.update('down-right')

    if  x < 0 and y < 0:
        self.update('up-left')
    if  x < 0 and y > 0:
        self.update('down-left')
  
  def verificar(self):
    if (pygame.draw.rect(self.screen, (255,255,255), (self.pantalla_x//2 - 3, self.pantalla_y//2 - 5,6,10)).colliderect(self.initX//2 - self.nave_rect[2]//4 + self.naveX + self.refuel_rect[2]//2 - self.s_rect[2]//2, self.initY//2 - (self.nave_rect[3]//14) + self.refuel_rect[3] +self.naveY + self.refuel_rect[3]//2 - self.s_rect[3]//2, self.s_rect[2], self.s_rect[3])):
      self.Alineado = True
      return True
    else: 
      self.Alineado = False
      return False
