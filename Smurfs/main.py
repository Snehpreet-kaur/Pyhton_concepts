import pgzrun
from random import randint

TITLE="SHOOT THE SMURF"

WIDTH = 600
HEIGHT = 400

message=""

smurf=Actor('smurf')
smurf.pos=250,250

background=Actor('bg')


def draw():
    screen.clear()
    background.draw()

    smurf.draw()
    screen.draw.text(message,center=(400,10),fontsize=50)

def place_smurf():
    smurf.x=randint(50,WIDTH - 50)
    smurf.y=randint(50,HEIGHT - 50)

def on_mouse_down(pos):
    global message
    if smurf.collidepoint(pos):
        place_smurf()
    else:
        message="You missed"

place_smurf()
pgzrun.go()