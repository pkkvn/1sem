import turtle as tr
import numpy as np

def circle(r):
    for i in range(180):
        tr.forward(2*r*np.sin(np.pi/360))
        tr.right(1)

def figure(r):
    circle(r)
    circle(r/10)
    

tr.shape('turtle')
tr.speed(0)

tr.left(90)
for i in range(5):
    figure(50)

