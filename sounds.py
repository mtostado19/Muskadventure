import pygame
from pygame import mixer

class sounds():
    def __init__(self):
      pygame.mixer.music.load('Assets/sound/city.mp3')
      pygame.mixer.music.set_volume(.2)
      pygame.mixer.music.play(-1)
    
    def stopSonido(self):
      pygame.mixer.music.fadeout(3000)
      pygame.time.delay(1000)

    def QuickStopSonido(self):
      pygame.mixer.music.fadeout(1000)
      pygame.time.delay(500)

    def lowStopSonido(self):
      pygame.mixer.music.fadeout(7000)

    def nivel1(self):
      pygame.mixer.music.load('Assets/sound/mountains.mp3')
      pygame.mixer.music.set_volume(1)
      pygame.mixer.music.play(1)

    def nivel2(self):
      pygame.mixer.music.load('Assets/sound/final-voyage.mp3')
      pygame.mixer.music.set_volume(.2)
      pygame.mixer.music.play(1)

    def nivel3(self):
      pygame.mixer.music.load('Assets/sound/musicPlataformer1.mp3')
      pygame.mixer.music.set_volume(.2)
      pygame.mixer.music.play(-1)
    
    def lavaSound(self):
      pygame.mixer.music.load('Assets/sound/musicPlataformer2.mp3')
      pygame.mixer.music.set_volume(.2)
      pygame.mixer.music.play(-1)
    
    def final(self):
      pygame.mixer.music.load('Assets/sound/time.mp3')
      pygame.mixer.music.set_volume(1)
      pygame.mixer.music.play(1)