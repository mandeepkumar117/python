# function->
# types->
# 1.)inbuilt function->print,type,set etc..


# types of argument->
# 1)possitional argument
# 2)keword argument
# 3) defoult arguments





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
# def add(x,y,z):
#     z=x+y+z 
#     # print(z)
#     return x,y,z
# p=int(input("enter first value: "))
# q=int(input("enter second number: "))
# r=int(input("enter third value: "))
# a,b,c=add(y=r,x=p,z=q)
# print(a)
# print(b)
# print(c)

# 3)
# def add(x=0,y=0,z=0):
#     z=x+y+z 
#     # print(z)
#     return x,y,z
# p=int(input("enter first value: "))
# q=int(input("enter second number: "))
# r=int(input("enter third value: "))
# c=add()
# c=add(p)
# c=add(p,q)
# c=add(p,q,r) 

# # 4.)variable_lenght argument(*n)

# def add(*n):
#     print(n)
#     sum=0
#     for i in n:
#         for x in i:
#             sum=sum+x
#     return sum
# x=eval(input("Enter any value: "))
# var1=add(x)
# print(var1)    