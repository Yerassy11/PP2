#Race!
import pygame
import random

pygame.init()


WIDTH, HEIGHT = 500, 700 #размеры экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game") #название игры
#установка нужныхнам компонентов
car_img = pygame.image.load("car.png")
coin_img = pygame.image.load("coin.png")
road_img = pygame.image.load("road.jpg")
#размеры машины и монеты
car_width, car_height = 70, 140
coin_width, coin_height = 40, 40

car_img = pygame.transform.scale(car_img, (car_width, car_height))
coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

#расположение обьектов
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5 

coin_x = random.randint(50, WIDTH - 50)
coin_y = -50
coin_speed = 10

score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

running = True
while running:
    screen.blit(road_img, (0, 0))
    screen.blit(car_img, (car_x, car_y))
    screen.blit(coin_img, (coin_x, coin_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #движение машины
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 10:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width - 10:
        car_x += car_speed
    #движение монеты
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(50, WIDTH - 50)

    if (car_x < coin_x < car_x + car_width or car_x < coin_x + coin_width < car_x + car_width) and \
            (car_y < coin_y < car_y + car_height or car_y < coin_y + coin_height < car_y + car_height):
        score += 1
        coin_y = -50
        coin_x = random.randint(50, WIDTH - 50)

    #показатель очков
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()