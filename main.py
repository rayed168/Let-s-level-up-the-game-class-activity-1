import pygame as pg
import sys
import random as rn
pg.init()
WIDTH=800
HEIGHT=600
screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Moving the sprite")
BLUE=(0,0,255)
WHITE=(255,255,255)
rect_width=50
rect_height=50
rect_x=WIDTH//2
rect_y=HEIGHT//2
rect_speed=5
running=True
while running:
    for event in pg.event.get():
        if pg.event==pg.QUIT:
            running=False
    keys=pg.key.get_pressed()
    if keys[pg.K_UP]:
        rect_y=rect_y - rect_speed
    if keys[pg.K_DOWN]:
        rect_y=rect_y + rect_speed
    if keys[pg.K_LEFT]:
        rect_x=rect_x - rect_speed
    if keys[pg.K_RIGHT]:
        rect_x=rect_x + rect_speed
    rect_x = max(0, min(WIDTH - rect_width, rect_x))
    rect_y = max(0, min(HEIGHT - rect_height, rect_y))   
    screen.fill(WHITE)
    pg.draw.rect(screen,BLUE,(rect_x,rect_y,rect_width,rect_height))
    pg.display.flip()
    pg.time.Clock().tick(30)
pg.quit()    
sys.exit()    