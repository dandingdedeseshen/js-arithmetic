
# 继承
class Father():
    def __init__(self,hp):
        self.hp = hp
    def fun(self):
        print(self.hp,'hahahahahh')


class Son(Father):
    def __init__(self,hp,lp):
        Father.__init__(self,hp)
        self.lp = lp
    def abc(self):
        # super(Son, self).fun()
        self.fun()
        print(self.lp,self.hp)

a = Son(3,4)
a.abc()