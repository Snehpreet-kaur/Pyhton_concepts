import pgzrun
from random import randint

WIDTH=500
HEIGHT=500

def draw():
    screen.fill("blue")
    
    #to draw a line
    screen.draw.line((20,0),(20,500),("teal"))

    #to draw the outline of a circle
    screen.draw.circle((150,50),50,("orange"))

    #to draw a filled circle
    screen.draw.filled_circle((250,50),50,("beige"))

    #to draw the outline of a rectangle
    #first mention the x and y and then the width and height
    Rectangle=Rect((50,100),(100,150))
    screen.draw.rect(Rectangle,("turquoise"))

    #to draw a filled rectangle
    Rectangle=Rect((180,100),(100,150))
    screen.draw.filled_rect(Rectangle,("pink"))

    #to draw text
    content="This is cool"
    screen.draw.text(content,[250,300])
    screen.draw.text("Thanks", (400, 400),fontsize= 20)

pgzrun.go()