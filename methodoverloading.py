class A:
    
    def Add(self,*n):
        sum=0
        for i in n:
            sum=sum+i
        return sum
    def Add(self,*n):
        return n
obj=A()
b=obj.Add(10,30)
print(b)
a=obj.Add(12,2,43)
print(a)    
    