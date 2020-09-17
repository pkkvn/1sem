import turtle as tr

def circle():
    for i in range(360):
        tr.forward(1)
        tr.left(1)
        
tr.shape('turtle')
tr.speed(0)

for i in range(6):
    circle()
    tr.left(60)
