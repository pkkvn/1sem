import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((800, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    vx = randint (-1,1)
    vy = randint (-1,1)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    if x == 0 or  x == 800:
        vx = -vx
    if y == 0 or y == 600:
        vy = -vy
    



points = 1    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = event.pos
            
            print('Click!')
            if (x - x0)**2 + (y - y0)**2 < r**2:
                print ('EST PROBITIE')
                print ('points = ', points)
                points += 1
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
