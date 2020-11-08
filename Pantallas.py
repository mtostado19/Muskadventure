import pygame

class pantallaUno():
  def __init__(self,screen):
    self.screen = screen
    self.cub = [
      pygame.image.load("Assets/T1.png"), #0
      pygame.image.load("Assets/S1.png"), #1
      pygame.image.load("Assets/S2.png"), #2
      pygame.image.load("Assets/S3.png"), #3
      pygame.image.load("Assets/S4.png"), #4
      pygame.image.load("Assets/BFR2.png"), #5
      pygame.image.load("Assets/FenceSM.png"), #6
      pygame.image.load("Assets/FenceSM2.png"), #7
      pygame.image.load("Assets/FenceSM3.png"), #8
      pygame.image.load("Assets/BarrelMini.png"), #9
      pygame.image.load("Assets/P2.png"), #10
      pygame.image.load("Assets/RoofEntrance.png"), #11
      pygame.image.load("Assets/Door.png"), #12
      pygame.image.load("Assets/BGpuerta1.png"), #13
      pygame.image.load("Assets/BGpuerta2.png"), #14
      pygame.image.load("Assets/RoofEntrance2.png"), #15
    ]
    self.cub_size = [
      64,   #Tamaño del terreno 0
      236,  #Nave               1
      74,   #Barrera            2
      50,   #Barril             3
    ]
    self.pantalla_X = 1152
    #self.pantalla_y = 768
    self.pantalla_y = 640

  def inicio(self):
    self.screen.blit(self.cub[2],[0,self.pantalla_y-self.cub_size[0]*2])
    self.screen.blit(self.cub[4],[0,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[2],[self.cub_size[0],self.pantalla_y-self.cub_size[0]*2])
    self.screen.blit(self.cub[4],[self.cub_size[0],self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[2],[self.cub_size[0]*2,self.pantalla_y-self.cub_size[0]*2])
    self.screen.blit(self.cub[4],[self.cub_size[0]*2,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*3,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*4,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*5,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*6,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*7,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*8,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*9,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*10,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*11,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*12,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*13,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*14,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*15,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*16,self.pantalla_y-self.cub_size[0]])
    self.screen.blit(self.cub[1],[self.cub_size[0]*17,self.pantalla_y-self.cub_size[0]])
    # Nave
    # self.screen.blit(self.cub[5],[0,self.pantalla_y-self.cub_size[0]*7-self.cub_size[1]])
    # Barrera
    self.screen.blit(self.cub[6],[self.cub_size[0]*3,self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[7],[self.cub_size[0]*4,self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[7],[self.cub_size[0]*5,self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[7],[self.cub_size[0]*6,self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[7],[self.cub_size[0]*7,self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[7],[self.cub_size[0]*8,self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[7],[self.cub_size[0]*9,self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[7],[self.cub_size[0]*10,self.pantalla_y-self.cub_size[0]-self.cub_size[2]])
    self.screen.blit(self.cub[8],[self.cub_size[0]*11,self.pantalla_y-self.cub_size[0]-self.cub_size[2]])

    #Entrada Edificio
    self.screen.blit(self.cub[10],[self.cub_size[0]*14, self.pantalla_y-(self.cub_size[0]*2)])
    self.screen.blit(self.cub[10],[self.cub_size[0]*15, self.pantalla_y-(self.cub_size[0]*2)])
    self.screen.blit(self.cub[10],[self.cub_size[0]*16, self.pantalla_y-(self.cub_size[0]*2)])
    self.screen.blit(self.cub[10],[self.cub_size[0]*17, self.pantalla_y-(self.cub_size[0]*2)])

    self.screen.blit(self.cub[14],[self.cub_size[0]*14, self.pantalla_y-(self.cub_size[0]*3)])
    self.screen.blit(self.cub[13],[self.cub_size[0]*15, self.pantalla_y-(self.cub_size[0]*3)])
    self.screen.blit(self.cub[14],[self.cub_size[0]*16, self.pantalla_y-(self.cub_size[0]*3)])
    self.screen.blit(self.cub[13],[self.cub_size[0]*17, self.pantalla_y-(self.cub_size[0]*3)])

    self.screen.blit(self.cub[15],[self.cub_size[0]*14, self.pantalla_y-(self.cub_size[0]*4)])
    self.screen.blit(self.cub[15],[self.cub_size[0]*15, self.pantalla_y-(self.cub_size[0]*4)])
    self.screen.blit(self.cub[11],[self.cub_size[0]*16, self.pantalla_y-(self.cub_size[0]*4)])
    self.screen.blit(self.cub[15],[self.cub_size[0]*17, self.pantalla_y-(self.cub_size[0]*4)])

    self.screen.blit(self.cub[12],[self.cub_size[0]*16, self.pantalla_y-(self.cub_size[0])-106])

    # Objetos
    self.screen.blit(self.cub[9],[self.cub_size[3]*10,self.pantalla_y-self.cub_size[0]-self.cub_size[3]])
    self.screen.blit(self.cub[9],[(self.cub_size[3]*11)-25,self.pantalla_y-self.cub_size[0]-self.cub_size[3]])
    self.screen.blit(self.cub[9],[(self.cub_size[3]*11)-37,self.pantalla_y-self.cub_size[0]-(self.cub_size[3]*2)])

class pantallaDos():
  def __init__(self,screen):
    self.screen = screen
    self.cub = [
      pygame.image.load("Assets/T1.png"),
      pygame.image.load("Assets/S1.png"),
      pygame.image.load("Assets/S2.png"),
      pygame.image.load("Assets/S3.png"),
      pygame.image.load("Assets/S4.png"),
      pygame.image.load("Assets/BarrelMini.png"),
      pygame.image.load("Assets/P2.png"),
      pygame.image.load("Assets/RoofEntrance.png"),
      pygame.image.load("Assets/Door.png"),
      pygame.image.load("Assets/BGpuerta1.png"),
      pygame.image.load("Assets/BGpuerta2.png"),
      pygame.image.load("Assets/RoofEntrance2.png"),
    ]
    self.cub_size = [
      64,   #Tamaño del terreno 0
      50,   #Barril             1
    ]
    self.pantalla_X = 1152
    #self.pantalla_y = 768
    self.pantalla_y = 640

  def Plataformer_Nivel2(self):
      pass
