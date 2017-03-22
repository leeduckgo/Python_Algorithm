#-*-coding:utf-8-*-
class Human:
    #类：人类Human；属性：身高height；方法，设置身高setHeight。
    def __init__(self):
        self.height=None
    def setHeight(self,meter):
    	self.height=meter
#============
aMan=Human()
aMan.setHeight(1.2)
print aMan.height
