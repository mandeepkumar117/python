class Gf:
    def dada(self,name):
        self.n=name
        print(self.n)
class P(Gf):
    def __init__(self,f_name):
        self.y=f_name
class C(P):
    def c_name(self,m_name):
        self.z=m_name
        print(self.z)
    
obj=C('neeraj')
obj.c_name("hello")
obj.dada("mandeep")