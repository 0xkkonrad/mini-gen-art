# this roughly follows generative art tutorials by Coding Cassowary https://www.youtube.com/playlist?list=PLBLV84VG7Md9oO4MUOhyqz7gBFOzx8XIw 


from turtle import *
import random

setup(1000, 1000)

tracer(0)

s = 10

def squiggle(x,y,s,l):
    if l == 0:
        return
    elif l % 2 == 0:
        goto(x,y)
        l -= 1
        squiggle(x+s,y,s,l)
    elif l % 2 == 1:
        goto(x,y)
        l -= 1
        squiggle(x,y+s,s,l)

def sea(x,y,s,l):
    if l == 0:
        return
    else:
        penup()
        goto(x,y)
        pendown()
        squiggle(x,y,s,200)
        l -= 1
        sea(x+s*2,y,s,l)

speed(1000)

sea(-1000,-500,s,100)

exitonclick()

