import pygame
import random
import xbox360_controller

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
    
    #Para Intro
    self.font = pygame.font.Font(None,30)
    self.nivel1 = pygame.image.load("Assets/nivel1.png")
    self.nivel1_image = self.nivel1.subsurface(self.nivel1.get_clip())
    self.nivel1_rect = self.nivel1_image.get_rect()

    self.instrucciones = pygame.image.load("Assets/instrucciones1.jpg")
    self.fallaste = pygame.image.load("Assets/fallaste.jpg")
    
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
        self.naveX += .150
    if direction == 'right':
        self.LastMovement = 'right'
        self.naveX -= .150

    if direction == 'up':
        self.LastMovement = 'up'
        self.naveY += .150
    if direction == 'down':
        self.LastMovement = 'down'
        self.naveY -= .150

    if direction == 'down-left':
        self.LastMovement = 'down-left'
        self.naveY -= .150
        self.naveX += .150
    if direction == 'down-right':
        self.LastMovement = 'down-right'
        self.naveY -= .150
        self.naveX -= .150

    if direction == 'up-right':
      self.LastMovement = 'up-right'
      self.naveY += .150
      self.naveX -= .150
    if direction == 'up-left':
      self.LastMovement = 'up-left'
      self.naveY += .150
      self.naveX += .150
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

  def ShowPrimerNivel(self):
    self.introEntrada()
    self.intro()
    self.introSalida()

    self.instruccionesEntrada()
    self.instruccionesFunc()
    self.instruccionesSalida()

    self.nivelEntrada()

  def introEntrada(self): 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(300 - alpha)
      self.screen.blit(self.nivel1,[(self.pantalla_x)//2 - self.nivel1_rect[2]//2, (self.pantalla_y)//2 - self.nivel1_rect[3]//2])
      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)

  def intro(self):
    current_time = pygame.time.get_ticks()
    endTime = current_time + 5000

    firstText = True;

    while firstText:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
        if event.type == pygame.MOUSEBUTTONDOWN:
          firstText = False
        if event.type == pygame.JOYBUTTONDOWN:
          if event.button == xbox360_controller.A:
            firstText = False
      self.screen.blit(self.nivel1,[(self.pantalla_x)//2 - self.nivel1_rect[2]//2, (self.pantalla_y)//2 - self.nivel1_rect[3]//2])
      self.clickInstruccion()
      pygame.display.update()
      
      tiempo = pygame.time.get_ticks()
      if tiempo >= endTime:
        firstText = False   
  
  def introSalida(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(alpha)
      self.screen.blit(self.nivel1,[(self.pantalla_x)//2 - self.nivel1_rect[2]//2, (self.pantalla_y)//2 - self.nivel1_rect[3]//2])
      self.screen.blit(self.fade, [0,0])
      self.clickInstruccion()
      pygame.display.update()
      pygame.time.delay(5)

  def instruccionesEntrada(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(300 - alpha)
      self.screen.blit(self.instrucciones, [0,0])
      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)
  
  def instruccionesFunc(self):
    current_time = pygame.time.get_ticks()
    endTime = current_time + 40000

    firstText = True;

    while firstText:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
        if event.type == pygame.MOUSEBUTTONDOWN:
          firstText = False
        if event.type == pygame.JOYBUTTONDOWN:
          if event.button == xbox360_controller.A:
            firstText = False
      self.screen.blit(self.instrucciones,[0,0])
      self.clickInstruccion()
      pygame.display.update()
      
      tiempo = pygame.time.get_ticks()
      if tiempo >= endTime:
        firstText = False  

  def instruccionesSalida(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(alpha)
      self.screen.blit(self.instrucciones,[0,0])
      self.screen.blit(self.fade, [0,0])
      self.clickInstruccion()
      pygame.display.update()
      pygame.time.delay(5)

  def nivelEntrada(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(300 - alpha)
      #Por mostrar
      self.screen.blit(self.nave, [self.initX//2 - self.nave_rect[2]//2 + self.naveX, self.initY//2 - self.nave_rect[3]//2 + self.naveY])
      self.screen.blit(self.refuel, [self.initX//2 - self.nave_rect[2]//4 + self.naveX , self.initY//2 - (self.nave_rect[3]//14) + self.refuel_rect[3] +self.naveY])
      if (self.Alineado):
        self.screen.blit(self.hudGreen,[0,0])  
      else:
        self.screen.blit(self.hudRed,[0,0])

      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)

  def nivelSalida(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(alpha)
      #Por mostrar:
      self.screen.blit(self.nave, [self.initX//2 - self.nave_rect[2]//2 + self.naveX, self.initY//2 - self.nave_rect[3]//2 + self.naveY])
      self.screen.blit(self.refuel, [self.initX//2 - self.nave_rect[2]//4 + self.naveX , self.initY//2 - (self.nave_rect[3]//14) + self.refuel_rect[3] +self.naveY])
      texto_final = self.font.render("Segundos para el encuentro: 0" ,True,(255,255,255))
      self.screen.blit(texto_final,[10,10])
      
      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)
  
  def restart(self):
    current_time = pygame.time.get_ticks()
    endTime = current_time + 5000

    firstText = True;

    while firstText:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
        if event.type == pygame.MOUSEBUTTONDOWN:
          firstText = False
        if event.type == pygame.JOYBUTTONDOWN:
          if event.button == xbox360_controller.A:
            firstText = False
      self.screen.blit(self.fallaste,[0,0])
      self.clickInstruccion()
      pygame.display.update()
      
      tiempo = pygame.time.get_ticks()
      if tiempo >= endTime:
        firstText = False 

  def restartEntrada(self):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
      self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
      self.fade.fill((0,0,0))
      for alpha in range(0,300):
        self.fade.set_alpha(300 - alpha)
        self.screen.blit(self.fallaste, [0,0])
        self.screen.blit(self.fade, [0,0])
        pygame.display.update()
        pygame.time.delay(5)

  def restartSalida(self):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
      self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
      self.fade.fill((0,0,0))
      for alpha in range(0,300):
        self.fade.set_alpha(alpha)
        self.screen.blit(self.fallaste,[0,0])
        self.screen.blit(self.fade, [0,0])
        self.clickInstruccion()
        pygame.display.update()
        pygame.time.delay(5)

  def showRestart(self):
    self.restartEntrada()
    self.restart()
    self.restartSalida()

  def clickInstruccion(self):
    self.texto_marcador = self.font.render(f"[Presione click o 'A' para continuar]", True, [255,255,255])
    self.texto_marcador_rect = self.texto_marcador.get_rect()
    self.screen.blit(self.texto_marcador, (self.pantalla_x - self.texto_marcador_rect[2] -10, self.pantalla_y - self.texto_marcador_rect[3]-10))