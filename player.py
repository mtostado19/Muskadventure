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
        self.left_states = {0:(5,41,28,39),1:(45,41,28,39),2:(85,41,28,39)}
        self.right_states = {0:(7,81,28,39),1:(47,81,28,39),2:(87,81,28,39)}
        #self.left_states = {0:(4,33,25,31),1:(36,33,25,31),2:(68,33,25,31)}
        #self.right_states = {0:(3,65,25,31),1:(35,65,25,31),2:(67,65,25,31)}

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

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            if self.rect.x > 0:
                self.rect.x -= 10
        if direction == 'right':
            self.clip(self.right_states)
            if self.rect.x < 1152:
                self.rect.x += 10

        if direction == "stand_left":
            self.clip(self.left_states[0])
        if direction == "stand_right":
            self.clip(self.right_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_SPACE:
                self.isJump = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.update("stand_left")
            if event.key == pygame.K_RIGHT:
                self.update("stand_right")

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -8:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 8
                self.rect.y += 5
        self.image = self.sheet.subsurface(self.sheet.get_clip())