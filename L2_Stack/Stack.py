#-*-coding:utf-8-*-
class Stack:
    def __init__(self):
        self.items = []
    #Stack()，创建一个空的薯片桶。

    def isEmpty(self):
        return self.items == []
    #isEmpty（），告诉你薯片桶是否为空。

    def push(self, item):
        self.items.append(item)
        #push(item)，在薯片桶里添加一片叫「item」的薯片。

    def pop(self):
        return self.items.pop()
    #pop()，去掉「薯片桶」最顶端的薯片，同时把那片薯片「给」你。

    def peek(self):
        return self.items[len(self.items)-1]
    #peek()，查看薯片顶端的那片薯片，但是将它保留在薯片桶里。

    def size(self):
        return len(self.items)
    #告诉你薯片桶里有多少片薯片。

#=========上面是栈类的定义，下面是栈的操作示例。============

s=Stack()
#生成一个薯片桶

print s.isEmpty()
#看看薯片桶是不是空的

s.push(5)
#将整数5装在薯片桶里

s.push('dog')
#将字符串「dog」装在薯片桶里

print s.isEmpty()
#看看薯片桶是不是空的

s.push(True)
#将「真」装在薯片桶里

print s.size()
#输出「薯片」的个数

print s.pop()
#去掉顶端薯片，并看看它是什么

print s.peek()
# 看看顶端的薯片，但不做任何操作
