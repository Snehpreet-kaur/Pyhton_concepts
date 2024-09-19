import pgzrun
from random import randint

WIDTH=500
HEIGHT=500

def draw():
    r=255
    g=0
    b=randint(0,255)
    screen.fill("teal")

    pos=250,250
    radius=20
    
    for i in range(60):
        screen.draw.circle(pos,radius,(r,g,b))
        radius=radius + 5
        r=r-2
        g=g+2
            
pgzrun.go()
