import pygame
##import pygame_gui

class background ():
  def __init__(self,screen):
    self.screen = screen
    self.fondo = pygame.image.load("Assets/Fondo.png")
    self.fondo_image = self.fondo.subsurface(self.fondo.get_clip())
    self.fondo_rect = self.fondo_image.get_rect()
    
    self.titulo = pygame.image.load("Assets/titulo.png")
    self.titulo_image = self.titulo.subsurface(self.titulo.get_clip())
    self.titulo_rect = self.titulo_image.get_rect()

    self.p1 = pygame.image.load("Assets/p1.png")
    self.p1_image = self.p1.subsurface(self.p1.get_clip())
    self.p1_rect = self.p1_image.get_rect()

    self.p2 = pygame.image.load("Assets/texto22.png")
    self.p2_image = self.p2.subsurface(self.p2.get_clip())
    self.p2_rect = self.p2_image.get_rect()

    self.nivel1 = pygame.image.load("Assets/nivel1.png")
    self.nivel1_image = self.nivel1.subsurface(self.nivel1.get_clip())
    self.nivel1_rect = self.nivel1_image.get_rect()

    self.play = pygame.image.load("Assets/play.png")
    self.play_rect = self.play.get_rect()
    
    self.font = pygame.font.Font(None,30)

    self.pantalla_X = 1152
    self.pantalla_y = 640

    ##self.manager = pygame_gui.UIManager((self.pantalla_X, self.pantalla_y))

  def clickInstruccion(self):
    self.texto_marcador = self.font.render(f"[Click para continuar]", True, [255,255,255])
    self.texto_marcador_rect = self.texto_marcador.get_rect()
    self.screen.blit(self.texto_marcador, (self.pantalla_X - self.texto_marcador_rect[2] -10, self.pantalla_y - self.texto_marcador_rect[3]-10))

  def Menu_entrada(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_X, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(300 - alpha)
      self.inicio()
      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)

  def inicio(self): 
    self.screen.blit(self.fondo,[0,0])
    self.screen.blit(self.titulo,[(self.pantalla_X)/2 - self.titulo_rect[2]/2, (self.pantalla_y)//4 - self.titulo_rect[3]/2])
    self.screen.blit(self.play,[(self.pantalla_X)/2 - self.play_rect[2]/2, (self.pantalla_y)//4*2 +30 - self.play_rect[3]/2])

  def Menu_salida(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_X, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(alpha)
      self.inicio()
      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)

    self.contarHistoria()
    
  def contarHistoria(self):
    self.EntradaHistoria()
    self.Historia1()
    self.SalidaHistoria()

    self.EntradaHistoria2()
    self.Historia2()
    self.SalidaHistoria2()

  def Historia1(self):

    current_time = pygame.time.get_ticks()
    endTime = current_time + 10000

    firstText = True;

    while firstText:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
        if event.type == pygame.MOUSEBUTTONDOWN:
          firstText = False

      self.screen.blit(self.p1,[(self.pantalla_X)//2 - self.p1_rect[2]//2, (self.pantalla_y)//2 - self.p1_rect[3]//2])
      self.clickInstruccion()
      pygame.display.update()
      
      tiempo = pygame.time.get_ticks()
      if tiempo >= endTime:
        firstText = False   
      
  def SalidaHistoria(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_X, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(alpha)
      self.screen.blit(self.p1,[(self.pantalla_X)//2 - self.p1_rect[2]//2, (self.pantalla_y)//2 - self.p1_rect[3]//2])
      self.screen.blit(self.fade, [0,0])
      self.clickInstruccion()
      pygame.display.update()
      pygame.time.delay(5)
  
  def EntradaHistoria(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_X, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(300 - alpha)
      self.screen.blit(self.p1,[(self.pantalla_X)//2 - self.p1_rect[2]//2, (self.pantalla_y)//2 - self.p1_rect[3]//2])
      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)

  def Historia2(self):

      current_time = pygame.time.get_ticks()
      endTime = current_time + 20000

      firstText = True;

      while firstText:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit
          if event.type == pygame.MOUSEBUTTONDOWN:
            firstText = False
          
        self.screen.blit(self.p2,[(self.pantalla_X)//2 - self.p2_rect[2]//2, (self.pantalla_y)//2 - self.p2_rect[3]//2])
        self.clickInstruccion()
        pygame.display.update()
        tiempo = pygame.time.get_ticks()
        if tiempo >= endTime:
          firstText = False   

  def SalidaHistoria2(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade1 = pygame.Surface((self.pantalla_X, self.pantalla_y//3 + 20))
    self.fade1.fill((0,0,0))
    self.fade2 = pygame.Surface((self.pantalla_X, self.pantalla_y//3))
    self.fade2.fill((0,0,0))
    for alpha in range(0,300):
      self.fade1.set_alpha(alpha)
      self.fade2.set_alpha(alpha)
      self.screen.blit(self.p2,[(self.pantalla_X)//2 - self.p2_rect[2]//2, (self.pantalla_y)//2 - self.p2_rect[3]//2])
      self.screen.blit(self.fade1, [0,0])
      self.screen.blit(self.fade2, [0,426])
      pygame.display.update()
      pygame.time.delay(5)
    
    endTime = pygame.time.get_ticks() + 3000
    delay = True
    while delay:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit
          if event.type == pygame.MOUSEBUTTONDOWN:
            delay = False
          
        pygame.time.delay(5)
        tiempo = pygame.time.get_ticks()
        if tiempo >= endTime:
          delay = False

    self.fade1.set_alpha(300)
    self.fade2.set_alpha(300)
    self.fade = pygame.Surface((self.pantalla_X, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(alpha)
      self.screen.blit(self.p2,[(self.pantalla_X)//2 - self.p2_rect[2]//2, (self.pantalla_y)//2 - self.p2_rect[3]//2])
      self.screen.blit(self.fade1, [0,0])
      self.screen.blit(self.fade2, [0,426])
      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)
  
  def EntradaHistoria2(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_X, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(300 - alpha)
      self.screen.blit(self.p2,[(self.pantalla_X)//2 - self.p2_rect[2]//2, (self.pantalla_y)//2 - self.p2_rect[3]//2])
      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)

  def primerNivelEntrada(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_X, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(300 - alpha)
      self.screen.blit(self.nivel1,[(self.pantalla_X)//2 - self.nivel1_rect[2]//2, (self.pantalla_y)//2 - self.nivel1_rect[3]//2])
      self.screen.blit(self.fade, [0,0])
      pygame.display.update()
      pygame.time.delay(5)

  def primerNivel(self):
    
    current_time = pygame.time.get_ticks()
    endTime = current_time + 5000

    firstText = True;

    while firstText:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
        if event.type == pygame.MOUSEBUTTONDOWN:
          firstText = False

      self.screen.blit(self.nivel1,[(self.pantalla_X)//2 - self.nivel1_rect[2]//2, (self.pantalla_y)//2 - self.nivel1_rect[3]//2])
      self.clickInstruccion()
      pygame.display.update()
      
      tiempo = pygame.time.get_ticks()
      if tiempo >= endTime:
        firstText = False   
  
  def primerNivelSalida(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit
    self.fade = pygame.Surface((self.pantalla_X, self.pantalla_y))
    self.fade.fill((0,0,0))
    for alpha in range(0,300):
      self.fade.set_alpha(alpha)
      self.screen.blit(self.nivel1,[(self.pantalla_X)//2 - self.nivel1_rect[2]//2, (self.pantalla_y)//2 - self.nivel1_rect[3]//2])
      self.screen.blit(self.fade, [0,0])
      self.clickInstruccion()
      pygame.display.update()
      pygame.time.delay(5)

  def ShowPrimerNivel(self):
    self.primerNivelEntrada()
    self.primerNivel()
    self.primerNivelSalida()