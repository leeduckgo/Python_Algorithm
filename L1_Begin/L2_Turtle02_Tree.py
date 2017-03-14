#-*- coding:utf-8 -*-
import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(25) #a
        tree(branchLen-15,t)
        #15是可调参数
        t.left(40) #b
        tree(branchLen-15,t)
        t.right(15) #c
        t.backward(branchLen)
        #a,b,c处参数皆可调，只用a+c=b即能生成树。


t = turtle.Turtle()
myWin = turtle.Screen()
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
#"green"可调，可以试试black，red等颜色
tree(75,t)
#75是可调参数
myWin.exitonclick()


