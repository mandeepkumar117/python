# function->
# types->
# 1.)inbuilt function->print,type,set etc..


# types of argument->
# 1)possitional argument
# 2)keword argument





# 1)
# def add(x,y,z):
#     z=x+y+z 
#     # print(z)
#     return z
# p=int(input("enter first value: "))
# q=int(input("enter second number: "))
# r=int(input("enter third value: "))
# s=add(p,q,r,10)
# print(s)

# 2)
def add(x,y,z):
    z=x+y+z 
    # print(z)
    return x,y,z
p=int(input("enter first value: "))
q=int(input("enter second number: "))
r=int(input("enter third value: "))
a,b,c=add(y=r,x=p,z=q)
print(a)
print(b)
print(c)