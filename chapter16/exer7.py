from turtle import Turtle
import time
MIN = 6.25
tl = Turtle()
def drawRuler(x,y,width,height):
    tl.speed(5)
    tl.up()
    tl.goto(x,y)
    tl.down()
    tl.forward(width)
    tl.up()
    tl.goto(x+width/2, y)
    tl.down()
    tl.left(90)
    tl.forward(height)
    tl.right(90)
    if height >= MIN:
        drawRuler(x+width/2, y, width/2, height/2)
        drawRuler(x, y, width/2, height/2)
drawRuler(10, 10, 100, 50)
time.sleep(3)
