class P:
    def __init__(self,p_name):
        self.x=p_name
    def p_properties(self,home,bank):
        self.h=home
        self.b=bank
class C(P):
    def c_properties(self,quali):
        self.q=quali
        print(self.h)
        print(self.b)
        print(self.q)
        print(self.x)
obj=C("mandeep")
obj.p_properties("bhopal","hdfc")
obj.c_properties("B.tech")                    