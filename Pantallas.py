import pygame
import xbox360_controller

class pantallaMarte():
  def __init__(self,screen):
    self.screen = screen
    self.cub = [
      pygame.image.load("Assets/superficieMarte.png"), #0
      pygame.image.load("Assets/stone1.png"), #1
      pygame.image.load("Assets/stone1_mini.png"), #2
      pygame.image.load("Assets/stone1_micro.png"), #3
    ]
    self.cub_size = [
      64,   #Tamaño del terreno 0
      38,   #altura de la roca 1
      26,   #altura de la roca mini
      7,    #altura de la roca micro

    ]
    self.pantalla_x = 1152
    self.pantalla_y = 640

  def superficieMarte(self):
    #piso
    self.screen.blit(self.cub[0], [0, self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + self.cub_size[0], self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*2), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*3), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*4), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*5), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*6), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*7), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*8), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*9), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*10), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*12), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*13), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*14), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*15), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*16), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*17), self.pantalla_y-self.cub_size[0]])

    #objetos
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*4), self.pantalla_y-self.cub_size[0]-self.cub_size[3]])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*7), self.pantalla_y-self.cub_size[0]-self.cub_size[3]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*10), self.pantalla_y-self.cub_size[0]-self.cub_size[1]])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*10)-30, self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*13), self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*13)+60, self.pantalla_y-self.cub_size[0]-self.cub_size[3]])

  def superficieMarteCueva(self):
    #Piso
    self.screen.blit(self.cub[0], [0, self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + self.cub_size[0], self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*2), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*3), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*4), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*5), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*6), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*7), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*8), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*9), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*10), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*12), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*16), self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*17), self.pantalla_y-self.cub_size[0]])

    #Objetos
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*3), self.pantalla_y-self.cub_size[0]-self.cub_size[1]])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*3)-30, self.pantalla_y-self.cub_size[0]-self.cub_size[2]])

class pantallaCuevaUno():
  def __init__(self,screen):
    self.screen = screen
    self.lavaIsUp = False
    self.lavaCount = 1
    self.cub = [
      pygame.image.load("Assets/Cave/plataformaC1.png"), #0
      pygame.image.load("Assets/Cave/plataformaC2.png"), #1
      pygame.image.load("Assets/Cave/plataformaC4.png"), #2
      pygame.image.load("Assets/Cave/plataformaC5.png"), #3
      pygame.image.load("Assets/Cave/plataformaC6.png"), #4
      pygame.image.load("Assets/Cave/plataformaC7.png"), #5
      pygame.image.load("Assets/Cave/plataformaC8.png"), #6
      pygame.image.load("Assets/Cave/plataformaC9.png"), #7
      pygame.image.load("Assets/Cave/plataformaC10.png"), #8
      pygame.image.load("Assets/Cave/plataformaC11.png"), #9
      pygame.image.load("Assets/Cave/plataformaC12.png"), #10
      pygame.image.load("Assets/Cave/cristal1.png"), #11
      pygame.image.load("Assets/Cave/roca2.png"), #12
      pygame.image.load("Assets/Cave/roca3.png"), #13
      pygame.image.load("Assets/LavaTostado.png"), #14
    ]
    self.cub_size = [
      36,   #Tamaño del terreno 0
      40,   #Altura del terreno
      18,   #Tamaño del terreno delgado
      60,   #Tamaño de la plataforma
      20,   #Tamaño del cristal
      180,  #Tamaño de roca 2
      260,  #Tamaño de roca 3
    ]
    self.pantalla_x = 1152
    self.pantalla_y = 640

  def Cueva1(self):
    #Objetos
    self.screen.blit(self.cub[11], [0 + self.cub_size[0], self.pantalla_y-(self.cub_size[1]*4) - self.cub_size[4]])
    self.screen.blit(self.cub[11], [0 + (self.cub_size[0]*6), self.pantalla_y-(self.cub_size[1]*12) - self.cub_size[4]])
    self.screen.blit(self.cub[11], [0 + (self.cub_size[0]*12), self.pantalla_y-(self.cub_size[1]*2) - self.cub_size[4]])
    self.screen.blit(self.cub[12], [0 + (self.cub_size[0]*8), self.pantalla_y-(self.cub_size[1]*8) - self.cub_size[5]])
    self.screen.blit(self.cub[13], [0 + (self.cub_size[0]*24), self.pantalla_y-self.cub_size[1] - self.cub_size[6]])

    #Primera plataforma
    self.screen.blit(self.cub[0], [0, self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[1], [0 + self.cub_size[2], self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[1], [0 + self.cub_size[0], self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*2), self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*3), self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*4), self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*5), self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*6), self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*7), self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*8), self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[0]*9), self.pantalla_y-(self.cub_size[1]*12)])

    #Segunda plataforma
    self.screen.blit(self.cub[8], [0 + (self.cub_size[0]*8)-self.cub_size[3], self.pantalla_y-(self.cub_size[1]*8)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*8), self.pantalla_y-(self.cub_size[1]*8)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*9), self.pantalla_y-(self.cub_size[1]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*10), self.pantalla_y-(self.cub_size[1]*8)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*11), self.pantalla_y-(self.cub_size[1]*8)])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*12), self.pantalla_y-(self.cub_size[1]*8)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*13), self.pantalla_y-(self.cub_size[1]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*14), self.pantalla_y-(self.cub_size[1]*8)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*15), self.pantalla_y-(self.cub_size[1]*8)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[0]*16), self.pantalla_y-(self.cub_size[1]*8)])

    self.screen.blit(self.cub[8], [0 + (self.cub_size[0]*16)-self.cub_size[3], self.pantalla_y-(self.cub_size[1]*10)])

    #Pared
    self.screen.blit(self.cub[5], [0 + (self.cub_size[0]*16), self.pantalla_y-(self.cub_size[1]*9)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[0]*16), self.pantalla_y-(self.cub_size[1]*10)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[0]*16), self.pantalla_y-(self.cub_size[1]*11)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[0]*16), self.pantalla_y-(self.cub_size[1]*12)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[0]*16), self.pantalla_y-(self.cub_size[1]*13)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[0]*16), self.pantalla_y-(self.cub_size[1]*14)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[0]*16), self.pantalla_y-(self.cub_size[1]*15)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[0]*16), self.pantalla_y-(self.cub_size[1]*16)])

    #Plataforma tres
    self.screen.blit(self.cub[2], [0, self.pantalla_y-(self.cub_size[1]*5)])
    self.screen.blit(self.cub[3], [0 + self.cub_size[0], self.pantalla_y-(self.cub_size[1]*5)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*2), self.pantalla_y-(self.cub_size[1]*5)])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*3), self.pantalla_y-(self.cub_size[1]*5)])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[0]*4), self.pantalla_y-(self.cub_size[1]*5)])

    self.screen.blit(self.cub[7], [0, self.pantalla_y-(self.cub_size[1]*7)])
    self.screen.blit(self.cub[7], [0, self.pantalla_y-(self.cub_size[1]*14)])

    #Plataforma cuatro
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*9), self.pantalla_y-(self.cub_size[1]*3)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*10), self.pantalla_y-(self.cub_size[1]*3)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*11), self.pantalla_y-(self.cub_size[1]*3)])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*12), self.pantalla_y-(self.cub_size[1]*3)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*13), self.pantalla_y-(self.cub_size[1]*3)])


    #Plataforma cinco
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*17), self.pantalla_y-(self.cub_size[1]*2)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*18), self.pantalla_y-(self.cub_size[1]*2)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*19), self.pantalla_y-(self.cub_size[1]*2)])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*20), self.pantalla_y-(self.cub_size[1]*2)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*21), self.pantalla_y-(self.cub_size[1]*2)])

    #Piso final
    self.screen.blit(self.cub[9], [0 + (self.cub_size[0]*23), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*24), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*25), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*26), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*27), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*28), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*29), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*30), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*31), self.pantalla_y-self.cub_size[1]])

    #LAVA
    if self.lavaIsUp == True:
      self.screen.blit(self.cub[14], [0, self.pantalla_y - (self.lavaCount * 36)+ self.lavaCount])

class pantallaCuevaDos():
  def __init__(self,screen):
    self.screen = screen
    self.lavaIsUp = False
    self.lavaCount = 1
    self.cub = [
      pygame.image.load("Assets/Cave/plataforma2C1.png"), #0
      pygame.image.load("Assets/Cave/plataforma2C2.png"), #1
      pygame.image.load("Assets/Cave/plataforma2C3.png"), #2
      pygame.image.load("Assets/Cave/plataforma2C4.png"), #3
      pygame.image.load("Assets/Cave/plataforma2C5.png"), #4
      pygame.image.load("Assets/Cave/plataforma2C6.png"), #5
      pygame.image.load("Assets/Cave/pilar1.png"), #6
      pygame.image.load("Assets/Cave/pilar2.png"), #7
      pygame.image.load("Assets/Cave/pilar3.png"), #8
      pygame.image.load("Assets/Cave/pilar4.png"), #9
      pygame.image.load("Assets/Cave/roca1.png"), #10
      pygame.image.load("Assets/Cave/roca4.png"), #11
      pygame.image.load("Assets/Cave/arbol1.png"), #12
      pygame.image.load("Assets/Cave/arbol2.png"), #13
      pygame.image.load("Assets/Cave/plataforma2C7.png"), #14
      pygame.image.load("Assets/Cave/block.png"), #15
      pygame.image.load("Assets/BotonOFF_mini.png"), #16
      pygame.image.load("Assets/BotonON_mini.png"), #17
      pygame.image.load("Assets/Cave/arbol3.png"), #18
      pygame.image.load("Assets/LibroTostado.png"), #19
      pygame.image.load("Assets/LavaTostado.png"), #20
    ]
    self.cub_size = [
      112,   #Tamaño del piso
      75,   #Altura del piso
      90,   #Ancho plataforma inicio
      36,   #Altura plataforma inicio
      40,   #Tamaño del cuadro piso
      70,   #Ancho 4 plataformas
      115,  #altura pilar
      140,  #altura piedra 1
      168,  #altura arbol 1
      138,  #altura arbol 2
      27,   #altura arbol 3
    ]
    self.pantalla_x = 1152
    self.pantalla_y = 640

  def Cueva2(self, pressed):
    #bloque
    if pressed == False:
      self.screen.blit(self.cub[15], [0 + (self.cub_size[3]), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[15], [0 + (self.cub_size[3]), self.pantalla_y-self.cub_size[0]-(self.cub_size[3])])
      self.screen.blit(self.cub[15], [0 + (self.cub_size[3]), self.pantalla_y-self.cub_size[0]-(self.cub_size[3]*2)])
      self.screen.blit(self.cub[15], [0 + (self.cub_size[3]), self.pantalla_y-self.cub_size[0]-(self.cub_size[3]*3)])

    #piedra
    self.screen.blit(self.cub[10], [0 + self.cub_size[5]* 12, self.pantalla_y - self.cub_size[1]- self.cub_size[7]])
    self.screen.blit(self.cub[11], [0 + self.cub_size[5]* 4, self.pantalla_y - self.cub_size[1]- self.cub_size[7]])

    #boton
    if pressed == False:
      self.screen.blit(self.cub[16], [0 + self.cub_size[5]*9, self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    else:
      self.screen.blit(self.cub[17], [0 + self.cub_size[5]*9, self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])

    #Pilares
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3)])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*4)])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*5)])

    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*14), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*14), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*14), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*14), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*4)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*14), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*5)])

    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*8), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*8), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[9], [0 + (self.cub_size[5]*8), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*10), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*10), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[8], [0 + (self.cub_size[5]*10), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3)])

    #piso inferior
    self.screen.blit(self.cub[0], [0, self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*2), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*3), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*4), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*5), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*6), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*7), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*8), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*9), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*10), self.pantalla_y-self.cub_size[1]])

    #piso inicio
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[4]*2), self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*13)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*13)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*13)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*12)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*12)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*12)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*11)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*11)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*10)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*10)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*10)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*9)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*9)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*9)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*8)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*8)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*7)])

    #4 plataformas
    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*3), self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*4), self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[5]*5)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*10)])

    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*13), self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*14), self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[5]*15)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*10)])

    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*3), self.pantalla_y-(self.cub_size[4]*5)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*4), self.pantalla_y-(self.cub_size[4]*5)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[5]*5)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*5)])

    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*13), self.pantalla_y-(self.cub_size[4]*5)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*14), self.pantalla_y-(self.cub_size[4]*5)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[5]*15)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*5)])

    #Platforma media
    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*7), self.pantalla_y-(self.cub_size[4]*7)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*8), self.pantalla_y-(self.cub_size[4]*7)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*9)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*7)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*10)-(self.cub_size[4]*2), self.pantalla_y-(self.cub_size[4]*7)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*11)-(self.cub_size[4]*3), self.pantalla_y-(self.cub_size[4]*7)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*12)-(self.cub_size[4]*4), self.pantalla_y-(self.cub_size[4]*7)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*13)-(self.cub_size[4]*5), self.pantalla_y-(self.cub_size[4]*7)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[5]*11)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*7)])

    #LAVA
    if self.lavaIsUp == True:
      self.screen.blit(self.cub[20], [0, self.pantalla_y - (self.lavaCount * 36)+ self.lavaCount])
  
  def Cueva3(self):

    #Pilares
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*5), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*5), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*5), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3)])
    self.screen.blit(self.cub[9], [0 + (self.cub_size[5]*5), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*4)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*9), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*9), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[8], [0 + (self.cub_size[5]*9), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3)])
    
    #arbol
    self.screen.blit(self.cub[12], [0, self.pantalla_y - self.cub_size[1] - self.cub_size[8]])
    self.screen.blit(self.cub[13], [90, self.pantalla_y - self.cub_size[1] - self.cub_size[9]])
    self.screen.blit(self.cub[13], [(self.cub_size[5]*13), self.pantalla_y-self.cub_size[9]-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[18], [(self.cub_size[5]*15), self.pantalla_y-self.cub_size[10]-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[18], [(self.cub_size[5]*15)-20, self.pantalla_y-self.cub_size[10]-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[18], [(self.cub_size[5]*15)+20, self.pantalla_y-self.cub_size[10]-(self.cub_size[4]*4)])

    #Plataforma inferior
    self.screen.blit(self.cub[0], [0, self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*2), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*3), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*4), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*5), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*6), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*7), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*8), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*9), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[0], [0 + (self.cub_size[0]*10), self.pantalla_y-self.cub_size[1]])

    #Plataforma inicio
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[4]*2), self.pantalla_y-(self.cub_size[3]*14)])

    #Plataforma media
    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*4), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*5), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*6)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*7)-(self.cub_size[4]*2), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*8)-(self.cub_size[4]*3), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*9)-(self.cub_size[4]*4), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*10)-(self.cub_size[4]*5), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*11)-(self.cub_size[4]*6), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*12)-(self.cub_size[4]*7), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*13)-(self.cub_size[4]*8), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*14)-(self.cub_size[4]*9), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*15)-(self.cub_size[4]*10), self.pantalla_y-(self.cub_size[4]*11)])
    self.screen.blit(self.cub[5], [0 + (self.cub_size[5]*16)-(self.cub_size[4]*11), self.pantalla_y-(self.cub_size[4]*11)])

    #Plataformas escalada
    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*13), self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*14), self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*15)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*16)-(self.cub_size[4]*2), self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*17)-(self.cub_size[4]*3), self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*18)-(self.cub_size[4]*4), self.pantalla_y-(self.cub_size[4]*10)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*19)-(self.cub_size[4]*5), self.pantalla_y-(self.cub_size[4]*10)])

    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*12), self.pantalla_y-(self.cub_size[4]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*13), self.pantalla_y-(self.cub_size[4]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*14)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*15)-(self.cub_size[4]*2), self.pantalla_y-(self.cub_size[4]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*16)-(self.cub_size[4]*3), self.pantalla_y-(self.cub_size[4]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*17)-(self.cub_size[4]*4), self.pantalla_y-(self.cub_size[4]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*18)-(self.cub_size[4]*5), self.pantalla_y-(self.cub_size[4]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*19)-(self.cub_size[4]*6), self.pantalla_y-(self.cub_size[4]*8)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*20)-(self.cub_size[4]*7), self.pantalla_y-(self.cub_size[4]*8)])

    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*11), self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*12), self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*13)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*14)-(self.cub_size[4]*2), self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*15)-(self.cub_size[4]*3), self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*16)-(self.cub_size[4]*4), self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*17)-(self.cub_size[4]*5), self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*18)-(self.cub_size[4]*6), self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*19)-(self.cub_size[4]*7), self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*20)-(self.cub_size[4]*8), self.pantalla_y-(self.cub_size[4]*6)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*21)-(self.cub_size[4]*9), self.pantalla_y-(self.cub_size[4]*6)])

    self.screen.blit(self.cub[4], [0 + (self.cub_size[5]*10), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*11), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*12)-self.cub_size[4], self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*13)-(self.cub_size[4]*2), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*14)-(self.cub_size[4]*3), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*15)-(self.cub_size[4]*4), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*16)-(self.cub_size[4]*5), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*17)-(self.cub_size[4]*6), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*18)-(self.cub_size[4]*7), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*19)-(self.cub_size[4]*8), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*20)-(self.cub_size[4]*9), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*21)-(self.cub_size[4]*10), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*22)-(self.cub_size[4]*11), self.pantalla_y-(self.cub_size[4]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[5]*23)-(self.cub_size[4]*12), self.pantalla_y-(self.cub_size[4]*4)])

    #pared
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), 0])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), self.cub_size[3]])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*8)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*9)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*10)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*11)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*12)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]), (self.cub_size[3]*13)])

    #LAVA
    if self.lavaIsUp == True:
      self.screen.blit(self.cub[20], [0, self.pantalla_y - (self.lavaCount * 36)+ self.lavaCount])


  def Cueva4(self):

    #arboles
    self.screen.blit(self.cub[18], [(self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]-self.cub_size[10]-(self.cub_size[6]*3)])
    self.screen.blit(self.cub[18], [(self.cub_size[5]*8), self.pantalla_y-self.cub_size[1]-self.cub_size[10]-(self.cub_size[6]*3)])
    self.screen.blit(self.cub[18], [(self.cub_size[5]*13), self.pantalla_y-self.cub_size[1]-self.cub_size[10]-(self.cub_size[6]*2)])

    #pilares
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[7], [0 + (self.cub_size[5]*4), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3)])

    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*6), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*6), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*6), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*6), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*6), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3.5)])

    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*8), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*8), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*8), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*8), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*3)])

    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*11), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*11), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*11), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*11), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2.5)])

    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*13), self.pantalla_y-self.cub_size[1]])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*13), self.pantalla_y-self.cub_size[1]-(self.cub_size[6])])
    self.screen.blit(self.cub[6], [0 + (self.cub_size[5]*13), self.pantalla_y-self.cub_size[1]-(self.cub_size[6]*2)])

    #Entrada
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[4]), self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[4]*2), self.pantalla_y-(self.cub_size[3]*14)])

    #Salida
    self.screen.blit(self.cub[3], [self.pantalla_x - self.cub_size[4], self.pantalla_y - (self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [self.pantalla_x - (self.cub_size[4]*2), self.pantalla_y - (self.cub_size[3]*7)])
    self.screen.blit(self.cub[14], [self.pantalla_x - (self.cub_size[4]*3), self.pantalla_y - (self.cub_size[3]*7)])

    #LAVA
    self.screen.blit(self.cub[20], [0, self.pantalla_y - 150 - (self.lavaCount * 36)])

  def Cueva5(self, pressed):
    #arboles
    #self.screen.blit(self.cub[12], [self.pantalla_x, self.pantalla_y - self.cub_size[1] - self.cub_size[8]])
    #self.screen.blit(self.cub[13], [90, self.pantalla_y - self.cub_size[1] - self.cub_size[9]])
    #self.screen.blit(self.cub[13], [(self.cub_size[5]*13), self.pantalla_y-self.cub_size[9]-(self.cub_size[4]*10)])
    #self.screen.blit(self.cub[18], [(self.cub_size[5]*15), self.pantalla_y-self.cub_size[10]-(self.cub_size[4]*4)])
    #self.screen.blit(self.cub[18], [(self.cub_size[5]*15)-20, self.pantalla_y-self.cub_size[10]-(self.cub_size[4]*4)])
    #self.screen.blit(self.cub[18], [(self.cub_size[5]*15)+20, self.pantalla_y-self.cub_size[10]-(self.cub_size[4]*4)])

    #Entrada
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*14)])

    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*8)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*8)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*8)])

    #Alrededor
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*15)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*15)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*15)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*16)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*16)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*16)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*17)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*17)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*17)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*18)])

    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [0, self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*2), self.pantalla_y-(self.cub_size[3])])

    self.screen.blit(self.cub[3], [(self.cub_size[3]*3), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*4), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*5), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*6), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*7), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*8), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*9), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*10), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*11), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*12), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*13), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*14), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*15), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*16), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*17), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*18), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*19), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*20), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*21), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*22), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*23), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*24), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*25), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*26), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*27), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*28), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*29), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*30), self.pantalla_y-(self.cub_size[3])])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3])])

    self.screen.blit(self.cub[3], [(self.cub_size[3]*3), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*4), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*5), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*6), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*7), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*8), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*9), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*10), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*11), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*12), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*13), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*14), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*15), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*16), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*17), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*18), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*19), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*20), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*21), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*22), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*23), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*24), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*25), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*26), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*27), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*28), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*29), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*30), self.pantalla_y-(self.cub_size[3]*18)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*18)])

    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*17)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*16)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*15)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*14)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*13)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*12)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*11)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*10)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*9)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*8)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*31), self.pantalla_y-(self.cub_size[3]*2)])

    #plataforma 1
    self.screen.blit(self.cub[3], [(self.cub_size[3]*3), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*4), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*5), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*6), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*3), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*4), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*5), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*6), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*3), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*4), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*5), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*6), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*3), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*4), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*5), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*6), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*3), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*4), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*5), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*6), self.pantalla_y-(self.cub_size[3]*2)])

    #boton
    if pressed == False:
      self.screen.blit(self.cub[19], [(self.cub_size[3]*15), self.pantalla_y-self.cub_size[1]-(self.cub_size[3]*6)])

    #plataforma central
    self.screen.blit(self.cub[3], [(self.cub_size[3]*7), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*8), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*9), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*10), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*11), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*12), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*13), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*14), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*15), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*16), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*17), self.pantalla_y-(self.cub_size[3]*7)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*18), self.pantalla_y-(self.cub_size[3]*7)])
    
    self.screen.blit(self.cub[3], [(self.cub_size[3]*7), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*8), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*9), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*10), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*11), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*12), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*13), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*14), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*15), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*16), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*17), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*18), self.pantalla_y-(self.cub_size[3]*6)])

    self.screen.blit(self.cub[3], [(self.cub_size[3]*7), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*8), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*9), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*10), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*11), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*12), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*13), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*14), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*15), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*16), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*17), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*18), self.pantalla_y-(self.cub_size[3]*5)])

    self.screen.blit(self.cub[3], [(self.cub_size[3]*7), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*8), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*9), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*10), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*11), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*12), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*13), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*14), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*15), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*16), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*17), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*18), self.pantalla_y-(self.cub_size[3]*4)])

    self.screen.blit(self.cub[3], [(self.cub_size[3]*7), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*8), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*9), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*10), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*11), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*12), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*13), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*14), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*15), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*16), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*17), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*18), self.pantalla_y-(self.cub_size[3]*3)])

    self.screen.blit(self.cub[3], [(self.cub_size[3]*7), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*8), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*9), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*10), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*11), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*12), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*13), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*14), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*15), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*16), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*17), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*18), self.pantalla_y-(self.cub_size[3]*2)])

    #plataforma 3
    self.screen.blit(self.cub[3], [(self.cub_size[3]*19), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*20), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*21), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*22), self.pantalla_y-(self.cub_size[3]*6)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*19), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*20), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*21), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*22), self.pantalla_y-(self.cub_size[3]*5)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*19), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*20), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*21), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*22), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*19), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*20), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*21), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*22), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*19), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*20), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*21), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*22), self.pantalla_y-(self.cub_size[3]*2)])

    self.screen.blit(self.cub[3], [(self.cub_size[3]*23), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*24), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*25), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*26), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*27), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*28), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*29), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*30), self.pantalla_y-(self.cub_size[3]*4)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*23), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*24), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*25), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*26), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*27), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*28), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*29), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*30), self.pantalla_y-(self.cub_size[3]*3)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*23), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*24), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*25), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*26), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*27), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*28), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*29), self.pantalla_y-(self.cub_size[3]*2)])
    self.screen.blit(self.cub[3], [(self.cub_size[3]*30), self.pantalla_y-(self.cub_size[3]*2)])

    #LAVA
    self.screen.blit(self.cub[20], [0, self.pantalla_y - (self.lavaCount * 36)+ self.lavaCount])

class Intrucciones():
    def __init__(self,screen):
        self.screen = screen
        self.pantalla_x = 1152
        self.pantalla_y = 640

        self.font = pygame.font.Font(None,40) ##
        self.instrucciones = pygame.image.load("Assets/instrucciones3.jpg")
        self.fallaste = pygame.image.load("Assets/fallaste.jpg")

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
            self.clickInstruccion()
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