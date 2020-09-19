import turtle as tr
import numpy as np

tr.shape('turtle')
tr.speed(0)


def one():
    tr.left(90)
    tr.forward(100)
    tr.left(135)
    tr.forward(50*np.sqrt(2))


def four():
    tr.left(90)
    tr.forward(100)
    tr.left(180)
    tr.forward(50)
    tr.right(90)
    tr.forward(50)
    tr.right(90)
    tr.forward(50)

def seven():
    tr.left(90)
    tr.forward(50)
    tr.right(45)
    tr.forward(50*np.sqrt(2))
    tr.left(135)
    tr.forward(50)

def zero():
    tr.forward(50)
    tr.left(90)
    tr.forward(100)
    tr.left(90)
    tr.forward(50)
    tr.left(90)
    tr.forward(100)


one()
tr.penup()
tr.goto(100,0)
tr.pendown()
tr.left(135)
four()
tr.penup()
tr.goto(200,0)
tr.pendown()
tr.right(90)
one()
tr.penup()
tr.goto(250,0)
tr.pendown()
tr.left(135)
seven()
tr.penup()
tr.goto(350,0)
tr.pendown()
tr.left(180)
zero()
tr.penup()
tr.goto(450,0)
tr.pendown()
tr.left(90)
zero()











    
    
