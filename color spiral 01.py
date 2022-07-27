# this roughly follows generative art tutorials by Coding Cassowary https://www.youtube.com/playlist?list=PLBLV84VG7Md9oO4MUOhyqz7gBFOzx8XIw 

from turtle import *
from theme import set_theme

# hsv is easier to understand and manipulate than rgb
from colorsys import hsv_to_rgb

set_theme()

r = 10
w = 20
revolutions = 20

width(w)

penup()
goto(0,-r)
pendown()

for angle in range(360*revolutions):
    pencolor(hsv_to_rgb(angle/3600, 0.75, 0.75))
    circle((angle/revolutions), 1)

exitonclick()