import turtle as tr
import numpy as np

tr.shape('turtle')
tr.speed(0)

def halfcircle(r):
    for i in range(180):
        tr.forward(2*r*np.sin(np.pi/360))
        tr.left(1)

def circle(r):
    halfcircle(r)
    halfcircle(r)

def xy(x, y):
    tr.penup()
    tr.goto(x, y)
    tr.pendown()

tr.right(180)
tr.left(180)

xy(0, -100)
tr.begin_fill()
circle(100)
tr.color('yellow')
tr.end_fill()

xy(50, 30)
tr.begin_fill()
circle(10)
tr.color('blue')
tr.end_fill()

xy(-50, 30)
tr.begin_fill()
circle(10)
tr.color('blue')
tr.end_fill()

xy(0, 10)
tr.right(90)
tr.color('black')
tr.width(10)
tr.forward(20)

xy(-30, -20)
tr.color('red')
halfcircle(40)
    
