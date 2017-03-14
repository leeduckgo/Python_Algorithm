#-*- coding:utf-8 -*-
import turtle

t = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        #上面的90是可调参数
        drawSpiral(myTurtle,lineLen-10)
        #上面的10是可调参数

drawSpiral(t,200)
#上面的200是可调参数
myWin.exitonclick()

