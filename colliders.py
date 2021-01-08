import pygame

class Colliders():
    def __init__(self):
        self.collidersLivel1 = [pygame.Rect(0, 576, 1152, 64)]
        self.collidersLivel2 = [
            pygame.Rect(0, 576, 824, 20),
            pygame.Rect(1040, 576, 128, 20),
        ]
        self.paredLeftCollider2 = [pygame.Rect(833, 576, 4, 60)]
        self.paredRightCollider2 = [
            pygame.Rect(1023, 576, 8, 60),
            pygame.Rect(1152, 0, 10, 640)
        ]
        self.collidersLevel3 = [
            pygame.Rect(0, 160, 378, 5),
            pygame.Rect(228, 320, 360, 5),
            pygame.Rect(0, 440, 208, 5),
            pygame.Rect(324, 520, 180, 5),
            pygame.Rect(612, 560, 180, 5),
            pygame.Rect(828, 600, 360, 5),
            pygame.Rect(516, 240, 60, 20),
            pygame.Rect(0, 360, 60, 20),
            pygame.Rect(0, 80, 60, 20)
        ]
        self.paredLeftCollider3 = [
            pygame.Rect(385, 170, 5, 36),
        ]
        self.paredRightCollider3 = [
            pygame.Rect(576, 0, 36, 288),
            #pygame.Rect(228, 320, 5, 36),
        ]

        self.collidersLevel4= [
            pygame.Rect(0, 565, 1152, 75),
            pygame.Rect(0, 136, 120, 36),
            pygame.Rect(230, 240, 150, 40),
            pygame.Rect(930, 240, 160, 40),
            pygame.Rect(230, 440, 160, 40),
            pygame.Rect(930, 440, 160, 40),
            pygame.Rect(510, 360, 280, 40),
        ]
        self.paredLeftCollider4 = [
            pygame.Rect(0, 0, 40, 100),
            pygame.Rect(76, 172, 36, 252),
            pygame.Rect(72, 420, 5, 144),
            #pygame.Rect(0, 0, 40, 100),
        ]
        self.paredRightCollider4 = [pygame.Rect(1116, 0, 5, 640)]
        self.collidersLevel5= [
            pygame.Rect(0, 565, 1152, 75),
            pygame.Rect(0, 136, 155, 10),
            pygame.Rect(280, 200, 460, 10),
            pygame.Rect(910, 240, 490, 10),
            pygame.Rect(840, 320, 490, 10),
            pygame.Rect(770, 400, 490, 10),
            pygame.Rect(700, 480, 490, 10),
        ]
        self.paredLeftCollider5 = [
            pygame.Rect(156, 136, 5, 10),
            pygame.Rect(0, 0, 40, 100),
        ]
        self.paredRightCollider5 = [pygame.Rect(1116, 0, 5, 496)]

        self.collidersLevel6= [
            pygame.Rect(0, 136, 156, 5),
            pygame.Rect(300, 220, 20, 5),
            pygame.Rect(440, 162.5, 20, 5),
            pygame.Rect(580, 220, 20, 5),
            pygame.Rect(790, 277.5, 20, 5),
            pygame.Rect(930, 335, 20, 5),
            pygame.Rect(1002, 388, 156, 5),
        ]
        self.paredLeftCollider6 = [
            pygame.Rect(321, 220, 5, 420),
            pygame.Rect(461, 162.5, 5, 477.5),
            pygame.Rect(601, 220, 5, 420),
            pygame.Rect(811, 277.5, 5, 362.5),
            pygame.Rect(951, 355, 5, 285),
        ]
        self.paredRightCollider6 = [
            pygame.Rect(279, 220, 5, 420),
            pygame.Rect(419, 162.5, 5, 477.5),
            pygame.Rect(559, 220, 5, 420),
            pygame.Rect(769, 277.5, 5, 362.5),
            pygame.Rect(909, 335, 5, 285),
        ]

        self.collidersLevel7= [
            pygame.Rect(0, 352, 108, 10),
            pygame.Rect(108, 424, 144, 10),
            pygame.Rect(252, 388, 432, 10),
            pygame.Rect(684, 424, 144, 10),
            pygame.Rect(828, 496, 288, 10),
        ]
        self.paredLeftCollider7 = [
            pygame.Rect(109, 352, 5, 72),
            pygame.Rect(686, 388, 5, 36),
            pygame.Rect(828, 424, 5, 144),
            pygame.Rect(0, 0, 40, 640),
        ]
        self.paredRightCollider7 = [
            pygame.Rect(250, 388, 1, 36),
            pygame.Rect(1116, 0, 5, 640),
        ]

        self.primerBoton = [pygame.Rect(600, 335, 80, 25)]
        self.segundoBoton = [pygame.Rect(520, 367, 80, 25)]
        self.numberOfPops = 0

        self.arboles1 = [
            pygame.Rect(0, 397, 260, 168), 
            pygame.Rect(910, 102, 220, 140),
            pygame.Rect(1050, 453, 102, 27)
        ]

        self.arboles2 = [
            pygame.Rect(280, 193, 40, 27),
            pygame.Rect(560, 193, 40, 27),
            pygame.Rect(910, 308, 40, 27),
        ]
