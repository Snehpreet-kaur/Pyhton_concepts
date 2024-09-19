import pgzrun
from random import randint

WIDTH=400
HEIGHT=400

def draw():
    r=255
    g=0
    b=randint(120,255)

    w=WIDTH
    h=HEIGHT - 200

    for i in range(20):
        rectangle=Rect((0,0),(w,h))
        rectangle.center=200,200
        screen.draw.rect(rectangle, (r, g, b))

        r -= 10
        g += 10

        w -=10
        h +=10


pgzrun.go()