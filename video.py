import pygame
import cv2

def video1(screen):
    video = "Assets/video/VideoIntroResized.mp4";
    pantalla_x = 1152
    pantalla_y = 640
    font = pygame.font.Font(None,30)
    texto_marcador = font.render(f"[Click para omitir]", True, [255,255,255])
    texto_marcador_rect = texto_marcador.get_rect()
    
    cap = cv2.VideoCapture(video)

    ret, img = cap.read()
    if not ret:
        print('couldnt open video')

    cap.set(3,pantalla_x)
    cap.set(4,pantalla_y)

    running = True
    playSound = True
    time = pygame.time.get_ticks() + 1000
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # read one frame and check if there was no problem
        ret, img = cap.read()
        if not ret:
            running = False
            break
        else:
            # transpose/rotate frame
            #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            #img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            img = cv2.transpose(img)
            ##print(img.shape)
            # blit directly on screen         
            cv2.waitKey(18)
            pygame.surfarray.blit_array(screen, img)
            screen.blit(texto_marcador, (pantalla_x - texto_marcador_rect[2] -10, pantalla_y - texto_marcador_rect[3]-10))
            currentTime = pygame.time.get_ticks()
    
        if currentTime >= time and playSound:
            pygame.mixer.music.load('Assets/sound/video.mp3')
            pygame.mixer.music.play(1)
            playSound = False
        print(pygame.time.get_ticks() - time)
        pygame.display.flip()