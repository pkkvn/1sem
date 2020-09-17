import turtle as tr
import numpy as np

def circle(r):
    for i in range(360):
        tr.forward(2*r*np.sin(np.pi/360))
        tr.left(1)
                   
tr.shape('turtle')
tr.speed(0)

tr.left(90)
for i in range(5):
    circle(i*10)
    tr.left(180)
    circle(i*10)
                   
                   
