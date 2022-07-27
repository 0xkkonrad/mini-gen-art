# this roughly follows generative art tutorials by Coding Cassowary https://www.youtube.com/playlist?list=PLBLV84VG7Md9oO4MUOhyqz7gBFOzx8XIw 


from turtle import *
from theme import set_theme

# hsv is easier to understand and manipulate than rgb
from colorsys import hsv_to_rgb

import random

tracer(False)

set_theme()

noise = 5
size = 100
shrink = 15

innerhue = 0.55
innerhuevar = 0.05

# draw square
def draw_square(x, y, s):
    penup()
    goto(x-s/2, y-s/2)
    pendown()
    for i in range(4):
        forward(s)
        left(90)

for x in range(-500+size//2,500, size):
    for y in range(-500+size//2,500, size):

        # determine offsets
        y_offset = random.randint(-noise, noise)
        x_offset = random.randint(-noise, noise)

        # draw inner squares with colour variation
        for i in range(6):
            # change hues of inner squares
            pencolor(hsv_to_rgb(innerhue+(i*innerhuevar), 0.5, 0.5))
            draw_square(x+i*x_offset, y+i*y_offset, size-i*shrink)
            
exitonclick()