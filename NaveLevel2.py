import pygame
import random
import xbox360_controller

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
        # Daño real
        self.sheet_explo = pygame.image.load("Assets/Level2/explo.png")
        self.image_explo = self.sheet_explo.subsurface(self.sheet_explo.get_clip())
        self.rect_explo = self.image_explo.get_rect()
        self.rect_explo.center = position

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
                self.rect.x -=2
                self.rect_daño.x -=2

        if self.rect.x < 1152-113:
            if direccion == 'right':
                self.rect.x +=2
                self.rect_daño.x +=2
        
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

    def moveConControl(self, x, y, A, B, X, Y):
        if x < 0 and y == 0:
            self.update('left')
        if x > 0 and y == 0:
            self.update('right')

        if  x > 0 and y < 0:
            self.update('right')
        if  x > 0 and y > 0:
            self.update('right')

        if  x < 0 and y < 0:
            self.update('left')
        if  x < 0 and y > 0:
            self.update('left')

        if X:
            self.update('LEFT')
        if B:
            self.update('RIGHT')
        if Y:
            self.update('UP')
        if A:
            self.update('DOWN')
            
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

class Intro():
    def __init__(self,screen):
        self.screen = screen
        self.pantalla_x = 1152
        self.pantalla_y = 640

        self.font = pygame.font.Font(None,40) ##
        self.instrucciones = pygame.image.load("Assets/instrucciones2.jpg")
        self.fallaste = pygame.image.load("Assets/fallaste.jpg")

        self.libro1 = pygame.image.load("Assets/libro1.jpg")
        self.libro2 = pygame.image.load("Assets/libro2.jpg")

        self.felicidades =  pygame.image.load("Assets/felicidades.jpg")
        self.fin =  pygame.image.load("Assets/fin.jpg")

    def showIntro(self):
        self.introEntrada()
        self.instruccionesFunc()
        self.instruccionesSalida()

    def introEntrada(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
        self.fade.fill((0,0,0))
        for alpha in range(0,300):
            self.fade.set_alpha(300 - alpha)
            self.screen.blit(self.instrucciones,[0,0])
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
            pygame.display.update()
            pygame.time.delay(5)
            
    def clickInstruccion(self):
        self.texto_marcador = self.font.render(f"[Presione click o 'A' para continuar]", True, [255,255,255])
        self.texto_marcador_rect = self.texto_marcador.get_rect()
        self.screen.blit(self.texto_marcador, (self.pantalla_x - self.texto_marcador_rect[2] -10, self.pantalla_y - self.texto_marcador_rect[3]-10))

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
            pygame.display.update()
            pygame.time.delay(5)

    def showRestart(self):
        self.restartEntrada()
        self.restart()
        self.restartSalida()

    def showLibro1(self):
        self.libro1Entrada()
        self.libro1Func()
        self.libro1Salida()

    def libro1Entrada(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
        self.fade.fill((0,0,0))
        for alpha in range(0,300):
            self.fade.set_alpha(300 - alpha)
            self.screen.blit(self.libro1, [0,0])
            self.screen.blit(self.fade, [0,0])
            pygame.display.update()
            pygame.time.delay(5)

    def libro1Func(self):
        current_time = pygame.time.get_ticks()
        endTime = current_time + 20000

        firstText = True;

        while firstText:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    firstText = False
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == xbox360_controller.A:
                        firstText = False

            self.screen.blit(self.libro1,[0,0])
            self.clickInstruccionLibro1()
            pygame.display.update()
        
            tiempo = pygame.time.get_ticks()
            if tiempo >= endTime:
                firstText = False 

    def libro1Salida(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
        self.fade.fill((0,0,0))
        for alpha in range(0,300):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.libro1 ,[0,0])
            self.screen.blit(self.fade, [0,0])
            pygame.display.update()
            pygame.time.delay(5)
    
    def showLibro2(self):
        self.libro2Entrada()
        self.libro2Func()
        self.libro2Salida()

    def libro2Entrada(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
        self.fade.fill((0,0,0))
        for alpha in range(0,300):
            self.fade.set_alpha(300 - alpha)
            self.screen.blit(self.libro2, [0,0])
            self.screen.blit(self.fade, [0,0])
            pygame.display.update()
            pygame.time.delay(5)

    def libro2Func(self):
        current_time = pygame.time.get_ticks()
        endTime = current_time + 60000

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
            self.screen.blit(self.libro2,[0,0])
            self.clickInstruccion()
            pygame.display.update()
        
            tiempo = pygame.time.get_ticks()
            if tiempo >= endTime:
                firstText = False 

    def libro2Salida(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
        self.fade.fill((0,0,0))
        for alpha in range(0,300):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.libro2 ,[0,0])
            self.screen.blit(self.fade, [0,0])
            pygame.display.update()
            pygame.time.delay(5)
    
    def clickInstruccionLibro1(self):
        self.texto_marcador = self.font.render(f"[Presione click o 'A' para traducir]", True, [255,255,255])
        self.texto_marcador_rect = self.texto_marcador.get_rect()
        self.screen.blit(self.texto_marcador, (self.pantalla_x - self.texto_marcador_rect[2] -10, self.pantalla_y - self.texto_marcador_rect[3]-10))

    def showFelicidades(self):
        self.felicidadesEntrada()
        self.felicidadesFunc()
        self.felicidadesSalida()
    
    def felicidadesFunc(self):
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

            self.screen.blit(self.felicidades,[0,0])
            self.clickInstruccion()
            pygame.display.update()
        
            tiempo = pygame.time.get_ticks()
            if tiempo >= endTime:
                firstText = False 

    def felicidadesEntrada(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
        self.fade.fill((0,0,0))
        for alpha in range(0,300):
            self.fade.set_alpha(300 - alpha)
            self.screen.blit(self.felicidades, [0,0])
            self.screen.blit(self.fade, [0,0])
            pygame.display.update()
            pygame.time.delay(5)

    def felicidadesSalida(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
        self.fade.fill((0,0,0))
        for alpha in range(0,300):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.felicidades,[0,0])
            self.screen.blit(self.fade, [0,0])
            pygame.display.update()
            pygame.time.delay(5)
    
    def showFin(self):
        self.finEntrada()
        self.finFunc()
        self.finSalida()
    
    def finFunc(self):
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

            self.screen.blit(self.fin,[0,0])
            self.clickInstruccionFin()
            pygame.display.update()
        
            tiempo = pygame.time.get_ticks()
            if tiempo >= endTime:
                firstText = False 

    def finEntrada(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
        self.fade.fill((0,0,0))
        for alpha in range(0,300):
            self.fade.set_alpha(300 - alpha)
            self.screen.blit(self.fin, [0,0])
            self.screen.blit(self.fade, [0,0])
            pygame.display.update()
            pygame.time.delay(5)

    def finSalida(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
        self.fade = pygame.Surface((self.pantalla_x, self.pantalla_y))
        self.fade.fill((0,0,0))
        for alpha in range(0,300):
            self.fade.set_alpha(alpha)
            self.screen.blit(self.fin,[0,0])
            self.screen.blit(self.fade, [0,0])
            pygame.display.update()
            pygame.time.delay(5)

    def clickInstruccionFin(self):
        self.texto_marcador = self.font.render(f"[Presione click o 'A' para terminar]", True, [255,255,255])
        self.texto_marcador_rect = self.texto_marcador.get_rect()
        self.screen.blit(self.texto_marcador, (self.pantalla_x - self.texto_marcador_rect[2] -10, self.pantalla_y - self.texto_marcador_rect[3]-10))