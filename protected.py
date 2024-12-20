class A:
    __x=10
    def __show(self):
        print("from class A")
class B(A):
    pass
# class C:
#     pass
print(dir(B))  
obj=B()
obj._A__show()     