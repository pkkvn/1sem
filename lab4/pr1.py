import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 20
screen = pygame.display.set_mode((800, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

X = 0
Y = 1
R = 2
COLOR = 3
VX = 4
VY = 5

WIDTH = 800
HEIGHT= 600

number = 50
balls = [0] * number


def draw(ball):
    circle(screen, ball[COLOR], (ball[X], ball[Y]), ball[R])


def new_ball():
   
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)

    vx = randint(-5, 5)
    vy = randint(-5, 5)

    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

    ball = [0] * 6
    ball[X] = x
    ball[Y] = y
    ball[VX] = vx
    ball[VY] = vy
    ball[R] = r
    ball[COLOR] = color
    return ball


def move_ball(ball):
    r = ball[R]
    x = ball[X]
    y = ball[Y]
    vx = ball[VX]
    vy = ball[VY]
    x += vx
    y += vy
    if x + r > WIDTH or x - r < 0:
        vx = -vx
        x += vx
        y += vy
    if y + r > HEIGHT or y - r < 0:
        vy = -vy
        x += vx
        y += vy
    else:
        x += vx
        y += vy

    ball[X] = x
    ball[Y] = y
    ball[VX] = vx
    ball[VY] = vy

    return ball


for i, ball in enumerate(balls):
    balls[i] = new_ball()

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
            for i, ball in enumerate(balls):
                x0, y0 = event.pos

                x = ball[X]
                y = ball[Y]
                r = ball[R]
                if (x - x0) ** 2 + (y - y0) ** 2 < r ** 2:
                    print('EST PROBITIE')
                    print('points = ', points)
                    points += 1
                    balls.remove(ball)

    for ball in balls:
        ball = move_ball(ball)
        draw(ball)

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()








    
    

