# this roughly follows generative art tutorials by Coding Cassowary https://www.youtube.com/playlist?list=PLBLV84VG7Md9oO4MUOhyqz7gBFOzx8XIw 


from turtle import *
from theme import set_theme

# hsv is easier to understand and manipulate than rgb
from colorsys import hsv_to_rgb

import random

tracer(False)

set_theme(canvas_width=600,pen_width=1)

size = 50
noise = 50
noisevar = -0.5

startinghue = 0.70
huevar = 0.02

for y in range(400,-400,-size):
    for x in range(-250,250,size):

        # randomize the color of the square
        r, g, b = hsv_to_rgb(startinghue+(huevar*random.random()), 1, 1)
        color(r, g, b)

        # move to the starting point
        penup()
        goto(x,y)
        pendown()

        if noise < 0:
            # draw the square
            for i in range(4):
                forward(size)
                right(90)

        else:
            #rotate
            angle = random.uniform(-noise,noise)
            right(angle)

            # draw the square
            for i in range(4):
                forward(size)
                right(90)

            left(angle)

            # adding noise as we go along
            noise += noisevar


exitonclick()