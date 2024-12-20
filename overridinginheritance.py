class A:
    def display(self):
        print("from class A")
class B(A):
    def display(self):
        print('from class b')
    def p(self):
        self.display()
        super().display()
obj=B()
obj.p()
obj.display()                    