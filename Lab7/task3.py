
import pygame as pg
import  sys

pg.init()
black=(0,0,0)
WIDTH=600
HEIGHT=400
speed=5
radius=20
circle_x=WIDTH//2
circle_y=HEIGHT//2
screen=pg.display.set_mode((WIDTH,HEIGHT))
clock=pg.time.Clock()
pg.display.set_caption("Moving-Circle")
running=True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False



    keys=pg.key.get_pressed()
    if keys[pg.K_RIGHT]: circle_x+=speed
    if keys[pg.K_LEFT]: circle_x -= speed
    if keys[pg.K_UP]: circle_y -= speed
    if keys[pg.K_DOWN]: circle_y += speed

    if circle_x-radius<0:
        circle_x=radius
    if circle_x+radius>WIDTH:
        circle_x=WIDTH-radius
    if circle_y+radius>HEIGHT:
        circle_y=HEIGHT-radius
    if circle_y-radius<0:
        circle_y=radius
    screen.fill((255,255,255))
    pg.draw.circle(screen,black,(circle_x,circle_y),radius)

    pg.display.flip()
    clock.tick(60)

pg.quit()
sys.exit()



