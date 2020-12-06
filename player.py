import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load("Assets/personajes/player1.png")
        #self.sheet.set_clip(pygame.Rect(0, 96, 30, 32))
        self.sheet.set_clip(pygame.Rect(45, 1, 31, 39))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.isJump = False
        self.jumpCount = 8
        self.momentum = 0
        self.plataformRect = []
        self.paredLeftRect = []
        self.paredRightRect = []
        self.direccion = [0,0]
        self.left_states = {0:(5,41,28,39),1:(45,41,28,39),2:(85,41,28,39)}
        self.right_states = {0:(7,81,28,39),1:(47,81,28,39),2:(87,81,28,39)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def check_pared(self, pared):
        cont = 0
        for c in pared:
            if self.rect.colliderect(c) == True:
                cont += 1
        if cont > 0:
            return True
        else:
            return False

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            check = self.check_pared(self.paredLeftRect)
            if self.rect.x > 0 and check == False:
                self.rect.x -= 10
                self.direccion[0] -= 10
        if direction == 'right':
            self.clip(self.right_states)
            check = self.check_pared(self.paredRightRect)
            if self.rect.x < 1152 and check == False:
                self.rect.x += 10
                self.direccion[0] += 10

        if direction == "stand_left":
            self.clip(self.left_states[0])
        if direction == "stand_right":
            self.clip(self.right_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event, colliders, left, right):
        if event.type == pygame.QUIT:
            game_over = True

        self.plataformRect = colliders
        self.paredLeftRect = left
        self.paredRightRect = right

        self.direccion = [0,0]
        self.rect.y += self.momentum
        self.momentum += 0.2
        if self.momentum > 6:
            self.momentum = 6

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                if self.jumpCount < 6:
                    self.momentum = -5

        self.direccion[1] = self.momentum

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.update("stand_left")
            if event.key == pygame.K_RIGHT:
                self.update("stand_right")

        prueba = self.movement()
        if prueba['bottom']:
            self.momentum = 0
            self.jumpCount = 0
        else:
            self.jumpCount += 1

    def collision_test(self):
        hit_list = []
        for tile in self.plataformRect:
            if self.rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def movement(self):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        c_list = self.collision_test()
        for tile in c_list:
            if self.direccion[1] > 0:
                self.rect.bottom = tile.top
                collision_types['bottom'] = True
            #elif self.direccion[1] < 0:
            #    self.rect.top = tile.bottom
            #    collision_types['top'] = True
        return collision_types