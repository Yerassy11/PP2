# Third task: Painter

import pygame

pygame.init()  # инициализация Pygame.

WIDTH, HEIGHT = 800, 600  # параметры экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # построение экрана
pygame.display.set_caption("Simple Paint in Pygame")  # название.

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# цвет по дефолту
current_color = BLACK

# заполнение фона белым цветом.
screen.fill(WHITE)

running = True
shape = "circle"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # закрытие игры
            running = False

        elif event.type == pygame.KEYDOWN:  # Значение принимаемые с клавиатуры
            if event.key == pygame.K_r:  # Если нажата R то рисуем квадрат
                shape = "rect"
            elif event.key == pygame.K_c:  #  Если нажата С то рисуем круг
                shape = "circle"
            elif event.key == pygame.K_e: #Если Е то ластик
                shape = "eraser"

            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = BLUE
            elif event.key == pygame.K_4:
                current_color = GREEN

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата мышка
            x, y = event.pos  # координаты мышки
            if shape == "circle":  # Если фигура это круг
                pygame.draw.circle(screen, current_color, (x, y), 20)
            elif shape == "rect":  # Если фигура это - четырехугольник болса
                pygame.draw.rect(screen, current_color, (x, y, 40, 40))
            elif shape == "eraser":  # Если включен ластик
                pygame.draw.circle(screen, WHITE, (x, y), 20)

    pygame.display.update()  # обновление экрана

pygame.quit()  #Закрытие Pygame.