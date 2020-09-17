import turtle as tr
import numpy as np

def mng(r, n):
    tr.penup()
    tr.goto(r, 0)
    tr.pendown()
    tr.left(90*(n+2)/n)
    for i in range(n):
        tr.forward(2*r*np.sin(np.pi/n))
        tr.left(360/n)
    tr.right(90*(n+2)/n)
    tr.penup()
    tr.goto(0, 0)
    tr.pendown()

for j in range(1, 10):
    mng(10*j, j+2)
