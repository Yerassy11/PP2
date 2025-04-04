# Third task: Painter

import pygame

pygame.init()  # инициализация Pygame.

WIDTH, HEIGHT = 600, 400  # параметры экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")
# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# фон
screen.fill(WHITE)
drawing = False
color = BLACK
mode = "circle"  # фигура по дефолту
clock = pygame.time.Clock()

running = True

# основная логика
while running:
    #обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        #рисование фигур
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key==pygame.K_t:
                mode="right_triangle"
            elif event.key==pygame.K_q:
                mode="equilateral_triangle"
            elif event.key==pygame.K_p:
                mode="rhombus"
            elif event.key == pygame.K_e:
                color = WHITE  # Eraser mode
            elif event.key == pygame.K_1:
                color = BLACK  # Black color
            elif event.key == pygame.K_2:
                color = RED  # Red color
            elif event.key == pygame.K_3:
                color = BLUE  # Blue color



        # изменения при нажатий клавиш
        if drawing:
            x, y = pygame.mouse.get_pos()  # координаты мышки
            if mode == "circle":
                pygame.draw.circle(screen, color, (x, y), 10)
            elif mode == "rectangle":
                pygame.draw.rect(screen, color, (x, y, 20, 20))
            elif mode== "right_triangle":
                pygame.draw.polygon(screen,color,[(x,y),(x,y+30),(x+30,y+30)])
            elif mode == "equilateral_triangle":
                pygame.draw.polygon(screen, color, [(x, y), (x - 25, y + 33), (x + 25, y + 33)])
            elif mode == "rhombus":
                pygame.draw.polygon(screen, color, [(x, y), (x + 20, y + 15), (x, y + 30), (x - 20, y + 15)])

        pygame.display.flip()
        clock.tick(60)

pygame.quit()  # Закрытие Pygame.