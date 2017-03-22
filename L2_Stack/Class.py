#-*-coding:utf-8-*-
class Human:
    #类：人类Human；特征（变量）：身高height；行为（函数）：设置身高setHeight。
    def __init__(self):
        self.height=None
    def setHeight(self,meter):
    	self.height=meter
#============
aMan=Human()
aMan.setHeight(1.2)
print aMan.height
