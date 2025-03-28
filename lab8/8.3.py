# Third task: Painter

import pygame

pygame.init()  # инициализация Pygame.
    
WIDTH, HEIGHT = 600, 400 #параметры экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")
#цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
#фон
screen.fill(WHITE)
drawing = False
color = BLACK
mode = "circle" #фигура по дефолту  
clock = pygame.time.Clock()

running = True

#основная логика
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_e:
                color = WHITE  # Eraser mode
            elif event.key == pygame.K_1:
                color = BLACK  # Black color
            elif event.key == pygame.K_2:
                color = RED  # Red color
            elif event.key == pygame.K_3:
                color = BLUE  # Blue color
        #изменения при нажатий клавиш
        if drawing:
            x, y = pygame.mouse.get_pos() #координаты мышки
            if mode == "circle":
                pygame.draw.circle(screen, color, (x, y), 10)
            elif mode == "rectangle":
                pygame.draw.rect(screen, color, (x, y, 20, 20))

        pygame.display.flip()
        clock.tick(60)


pygame.quit()  #Закрытие Pygame.
