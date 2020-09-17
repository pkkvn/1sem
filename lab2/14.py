import turtle as tr
import numpy as np

tr.shape('turtle')
tr.speed(0)

n = int(input())

def zv():
    tr.forward(100)
    tr.left(180*(1-1/n))

for i in range(n):
    zv()
