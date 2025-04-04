#First task:Race!
import pygame
import random

pygame.init()

# настройки окна
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game with Weights & Enemy")

#заргузка изображений
car_img = pygame.image.load("car.png")
coin_img = pygame.image.load("coin.png")
road_img = pygame.image.load("road.jpg")
enemy_img = pygame.image.load("car_.png")  # Добавим картинку "противника"

# параметры
car_width, car_height = 70, 140
coin_width, coin_height = 40, 40
enemy_width, enemy_height = 60, 120

#масштабируем изображения
car_img = pygame.transform.scale(car_img, (car_width, car_height))
coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
enemy_img = pygame.transform.scale(enemy_img, (enemy_width, enemy_height))

# координаты и скорости
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 8


coin = {
    "x": random.randint(50, WIDTH - 50),
    "y": -50,
    "speed": 10,
    "weight": random.randint(1, 3)  # случайный "вес" монеты (1, 2 или 3 очка)
}

#противник, его машина будет двигаться сверху вниз
enemy_x = random.randint(50, WIDTH - 50)
enemy_y = -150
enemy_speed = 10  # скорость врага

score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

running = True

# Какое количество очков нужно собрать, чтобы ускорить противника
n2_lvl_up = 5

while running:
    # Рисуем фон (дорогу)
    screen.blit(road_img, (0, 0))
    # Рисуем нашу машину
    screen.blit(car_img, (car_x, car_y))
    # Рисуем монету
    screen.blit(coin_img, (coin["x"], coin["y"]))
    # Рисуем машину-противника
    screen.blit(enemy_img, (enemy_x, enemy_y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 10:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width - 10:
        car_x += car_speed


    coin["y"] += coin["speed"]
    # Если монета улетела за нижний край, генерируем новую
    if coin["y"] > HEIGHT:
        coin["y"] = -50
        coin["x"] = random.randint(50, WIDTH - 50)
        coin["weight"] = random.randint(1, 3)


    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    coin_rect = pygame.Rect(coin["x"], coin["y"], coin_width, coin_height)

    if car_rect.colliderect(coin_rect):

        score += coin["weight"]

        coin["y"] = -50
        coin["x"] = random.randint(50, WIDTH - 50)
        coin["weight"] = random.randint(1, 3)

        # Если счёт стал кратен n2_lvlup, увеличиваем скорость врага
        if score % n2_lvl_up == 0:
            enemy_speed += 2  # ускоряем врага на 2

    #движение противника
    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -150
        enemy_x = random.randint(50, WIDTH - 50)


    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    if car_rect.colliderect(enemy_rect):
        # Если сталкиваемся с врагом, считаем, что игра окончена
        running = False


    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Обновляем экран
    pygame.display.update()

    clock.tick(30)

pygame.quit()
