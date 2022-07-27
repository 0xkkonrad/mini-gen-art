# this roughly follows generative art tutorials by Coding Cassowary https://www.youtube.com/playlist?list=PLBLV84VG7Md9oO4MUOhyqz7gBFOzx8XIw 


from turtle import *
from theme import set_theme
from colorsys import hsv_to_rgb

set_theme()

RADIUS = 300
WIDTH = 100

width(WIDTH)

penup()
goto(0,-RADIUS)
pendown()

for angle in range(360):
    pencolor(hsv_to_rgb(angle / 360, 0.75, 0.75))
    circle(RADIUS, 1)

exitonclick()