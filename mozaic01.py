# this roughly follows generative art tutorials by Coding Cassowary https://www.youtube.com/playlist?list=PLBLV84VG7Md9oO4MUOhyqz7gBFOzx8XIw 


from turtle import *
import random

setup(1000, 1000)
tracer(0,0)

def tiling(x,y,s,l,mode):

    if mode == "straight":
        if l == 0:
            #vertical
            if random.random() < 0.5:
                penup()
                goto(x, y-s)
                pendown()
                goto(x, y+s)

            # horizontal
            else:
                penup()
                goto(x-s, y)
                pendown()
                goto(x+s, y)

        # split screen and go to next level
        else:
            s = s/2
            l = l-1
            tiling(x-s, y-s, s, l,mode)
            tiling(x+s, y-s, s, l,mode)
            tiling(x-s, y+s, s, l,mode)
            tiling(x+s, y+s, s, l,mode)        

    elif mode == "diagonal":
        if l == 0:
            if random.random() < 0.5:
                penup()
                goto(x-s, y+s)
                pendown()
                goto(x+s, y-s)

            else:
                penup()
                goto(x-s, y-s)
                pendown()
                goto(x+s, y+s)

        # split screen and go to next level
        else:
            s = s/2
            l = l-1
            tiling(x-s, y-s, s, l,mode)
            tiling(x+s, y-s, s, l,mode)
            tiling(x-s, y+s, s, l,mode)
            tiling(x+s, y+s, s, l,mode)        


tiling(0,0,400,4,"diagonal")



exitonclick()

