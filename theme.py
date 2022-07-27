from turtle import *

from colorsys import hsv_to_rgb


def set_theme(canvas_width = 1000,
              canvas_height = 1000,
              background_color = ("grey"),	
              pen_color = ("brown"),
              pen_width = 3):
    setup(canvas_width, canvas_height)
    width(pen_width)
    bgcolor(background_color)
    pencolor(pen_color)
    tracer(20)
    hideturtle()
    return canvas_width, canvas_height, background_color, pen_color, pen_width