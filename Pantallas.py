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
      pygame.image.load("Assets/S2.png"), #0
      pygame.image.load("Assets/S3.png"), #1
      pygame.image.load("Assets/Box_s.png"), #2
      pygame.image.load("Assets/P2.png"), #3
      pygame.image.load("Assets/RoofEntrance.png"), #4
      pygame.image.load("Assets/RoofEntrance2.png"), #5
      pygame.image.load("Assets/Door.png"), #6
      pygame.image.load("Assets/BGpuerta1.png"), #7
      pygame.image.load("Assets/BGpuerta2.png"), #8
      pygame.image.load("Assets/Escaleras1_Mini.png"), #9
      pygame.image.load("Assets/S2_floating.png"), #10
    ]
    self.cub_size = [
      64,   #Tamaño del terreno 0
      50,   #Barril             1
      58,   #Puerta             2
    ]
    self.pantalla_X = 1152
    #self.pantalla_y = 768
    self.pantalla_y = 640

  def Plataformer_Nivel2(self):
      #Techo nivel superior
      self.screen.blit(self.cub[5],[0, 0])
      self.screen.blit(self.cub[4],[(self.cub_size[0]), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*2), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*3), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*4), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*5), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*6), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*7), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*8), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*9), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*10), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*11), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*12), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*13), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*14), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*15), 0])
      self.screen.blit(self.cub[4],[(self.cub_size[0]*16), 0])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*17), 0])

      #Piso nivel superior
      self.screen.blit(self.cub[3],[0, (self.cub_size[0]*2) ])
      self.screen.blit(self.cub[3],[(self.cub_size[0]), (self.cub_size[0]*2)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*2), (self.cub_size[0]*2)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*3), (self.cub_size[0]*2)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*4), (self.cub_size[0]*2)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*5), (self.cub_size[0]*2)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*6), (self.cub_size[0]*2)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*7), (self.cub_size[0]*2)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*8), (self.cub_size[0]*2)])

      #Techo nivel intermedio
      self.screen.blit(self.cub[5],[0, (self.cub_size[0]*3)])
      self.screen.blit(self.cub[4],[(self.cub_size[0]), (self.cub_size[0]*3)])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*2), (self.cub_size[0]*3)])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*3), (self.cub_size[0]*3)])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*4), (self.cub_size[0]*3)])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*5), (self.cub_size[0]*3)])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*6), (self.cub_size[0]*3)])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*7), (self.cub_size[0]*3)])
      self.screen.blit(self.cub[5],[(self.cub_size[0]*8), (self.cub_size[0]*3)])

      #Piso nivel intermedio
      self.screen.blit(self.cub[3],[(self.cub_size[0]*3), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*4), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*5), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*6), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*7), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*8), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*9), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*10), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*11), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*12), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*13), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*14), (self.cub_size[0]*5)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*15), (self.cub_size[0]*5)])

      #Piso nivel Inferior
      self.screen.blit(self.cub[0],[0, self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[0],[(self.cub_size[0]), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*3), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*5), self.pantalla_y-(self.cub_size[0]*2)])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*6), self.pantalla_y-(self.cub_size[0]*2)])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*7), self.pantalla_y-(self.cub_size[0]*2)])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*8), self.pantalla_y-(self.cub_size[0]*2)])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*9), self.pantalla_y-(self.cub_size[0]*2)])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*10), self.pantalla_y-(self.cub_size[0]*2)])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*12), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*14), self.pantalla_y-(self.cub_size[0]*2)])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*16), self.pantalla_y-(self.cub_size[0]*3)])
      self.screen.blit(self.cub[0],[(self.cub_size[0]*17), self.pantalla_y-(self.cub_size[0]*4)])


      #Background Inferior
      self.screen.blit(self.cub[1],[(self.cub_size[0]*2), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*4), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*5), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*6), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*7), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*8), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*9), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*10), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*13), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*14), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*15), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*16), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*16), self.pantalla_y-(self.cub_size[0]*2)])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*17), self.pantalla_y-self.cub_size[0]])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*17), self.pantalla_y-(self.cub_size[0]*2)])
      self.screen.blit(self.cub[1],[(self.cub_size[0]*17), self.pantalla_y-(self.cub_size[0]*3)])

      #Plataformas
      self.screen.blit(self.cub[10],[(self.cub_size[0]*12), self.pantalla_y-(self.cub_size[0]*5)])
      self.screen.blit(self.cub[10],[(self.cub_size[0]*14), self.pantalla_y-(self.cub_size[0]*6)])
      self.screen.blit(self.cub[10],[(self.cub_size[0]*12), self.pantalla_y-(self.cub_size[0]*7)])
      self.screen.blit(self.cub[10],[(self.cub_size[0]*14), self.pantalla_y-(self.cub_size[0]*8)])
      self.screen.blit(self.cub[10],[(self.cub_size[0]*12), self.pantalla_y-(self.cub_size[0]*9)])

      #Seccion final
      self.screen.blit(self.cub[3],[(self.cub_size[0]*15), (self.cub_size[0]*2)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*16), (self.cub_size[0]*2)])
      self.screen.blit(self.cub[3],[(self.cub_size[0]*17), (self.cub_size[0]*2)])


      #Seccion Bloqueada
      self.screen.blit(self.cub[2],[(self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*5)-8])
      self.screen.blit(self.cub[2],[(self.cub_size[0]*11)-self.cub_size[1], self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*5)-8])
      self.screen.blit(self.cub[2],[(self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*6)-8])
      self.screen.blit(self.cub[2],[(self.cub_size[0]*11)-self.cub_size[1], self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*6)-8])
      self.screen.blit(self.cub[2],[(self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*7)-8])
      self.screen.blit(self.cub[2],[(self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*8)-8])
      self.screen.blit(self.cub[2],[(self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*9)-8])
      self.screen.blit(self.cub[2],[(self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*10)-9])
      self.screen.blit(self.cub[2],[(self.cub_size[0]*11), self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*11)-9])

      #Objetos
      # -- Escaleras --
      self.screen.blit(self.cub[9],[(self.cub_size[0]*14)-40, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*5)-8])
      self.screen.blit(self.cub[9],[(self.cub_size[0]*14)-40, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*6)-8])
      self.screen.blit(self.cub[9],[(self.cub_size[0]*14)-40, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*7)-8])
      self.screen.blit(self.cub[9],[(self.cub_size[0]*14)-40, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*8)-8])
      self.screen.blit(self.cub[9],[(self.cub_size[0]*14)-40, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*9)-8])

      self.screen.blit(self.cub[9],[(self.cub_size[0]*9)+10, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*5)-8])
      self.screen.blit(self.cub[9],[(self.cub_size[0]*9)+10, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*6)-8])
      self.screen.blit(self.cub[9],[(self.cub_size[0]*9)+10, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*7)-8])
      self.screen.blit(self.cub[9],[(self.cub_size[0]*9)+10, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*8)-8])
      self.screen.blit(self.cub[9],[(self.cub_size[0]*9)+10, self.pantalla_y-self.cub_size[0]-(self.cub_size[1]*9)-8])
      # -- Puertas --
      self.screen.blit(self.cub[6],[self.cub_size[0], self.pantalla_y-(self.cub_size[0]*8)-(self.cub_size[2])])
      self.screen.blit(self.cub[6],[self.cub_size[0]*16, self.pantalla_y-(self.cub_size[0]*8)-(self.cub_size[2])])
      #  -- Pared de Fondo --
      self.screen.blit(self.cub[8], [0, self.cub_size[0]])
      self.screen.blit(self.cub[7], [(self.cub_size[0]*2), self.cub_size[0]])
      self.screen.blit(self.cub[8], [(self.cub_size[0]*3), self.cub_size[0]])
      self.screen.blit(self.cub[7], [(self.cub_size[0]*4), self.cub_size[0]])
      self.screen.blit(self.cub[8], [(self.cub_size[0]*5), self.cub_size[0]])
      self.screen.blit(self.cub[7], [(self.cub_size[0]*6), self.cub_size[0]])
      self.screen.blit(self.cub[8], [(self.cub_size[0]*7), self.cub_size[0]])
      self.screen.blit(self.cub[7], [(self.cub_size[0]*8), self.cub_size[0]])

      self.screen.blit(self.cub[8], [(self.cub_size[0]*15), self.cub_size[0]])
      self.screen.blit(self.cub[7], [(self.cub_size[0]*17), self.cub_size[0]])

      self.screen.blit(self.cub[8], [(self.cub_size[0]*3), self.cub_size[0]*4])
      self.screen.blit(self.cub[7], [(self.cub_size[0]*4), self.cub_size[0]*4])
      self.screen.blit(self.cub[8], [(self.cub_size[0]*5), self.cub_size[0]*4])
      self.screen.blit(self.cub[7], [(self.cub_size[0]*6), self.cub_size[0]*4])
      self.screen.blit(self.cub[8], [(self.cub_size[0]*7), self.cub_size[0]*4])
      self.screen.blit(self.cub[7], [(self.cub_size[0]*8), self.cub_size[0]*4])

      # -- Barriles --

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

    #Plataforma cuatro
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*9), self.pantalla_y-(self.cub_size[1]*3)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*10), self.pantalla_y-(self.cub_size[1]*3)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*11), self.pantalla_y-(self.cub_size[1]*3)])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*12), self.pantalla_y-(self.cub_size[1]*3)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*13), self.pantalla_y-(self.cub_size[1]*3)])


    #Plataforma cinco
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*17), self.pantalla_y-(self.cub_size[1]*4)])
    self.screen.blit(self.cub[3], [0 + (self.cub_size[0]*18), self.pantalla_y-(self.cub_size[1]*4)])
    self.screen.blit(self.cub[4], [0 + (self.cub_size[0]*19), self.pantalla_y-(self.cub_size[1]*4)])
    self.screen.blit(self.cub[1], [0 + (self.cub_size[0]*20), self.pantalla_y-(self.cub_size[1]*4)])
    self.screen.blit(self.cub[2], [0 + (self.cub_size[0]*21), self.pantalla_y-(self.cub_size[1]*4)])

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

class pantallaCuevaDos():
  def __init__(self,screen):
    self.screen = screen
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
    ]
    self.pantalla_x = 1152
    self.pantalla_y = 640

  def Cueva2(self):
    #piedra
    self.screen.blit(self.cub[10], [0 + self.cub_size[5]* 12, self.pantalla_y - self.cub_size[1]- self.cub_size[7]])
    self.screen.blit(self.cub[11], [0 + self.cub_size[5]* 4, self.pantalla_y - self.cub_size[1]- self.cub_size[7]])

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


  def Cueva4(self):
    #LAVA


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

  def Cueva5(self):
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