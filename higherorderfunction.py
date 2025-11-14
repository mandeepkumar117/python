# hierorder function->when we pass function as a argument then we called hierorder function

# hierorderfunction->map.filter,reduce
# here start from map function
# mylist=[10,20,30,40,50]
# def dec(x):
#     return x **2
# x=map(dec,mylist)
# print(tuple(x))


# here start from filter
# mytupple=(44,34,56,50,60,67,70,90)
# def greater_60(x):
#     if x>60:
#         return x
# x=list(filter(greater_60,mytupple))
# print(x)    


# here start from reduce

# import functools 
    #   or
# from functools import reduce
# from functools import reduce

import functools as new

mytuple=(10,20,30,80,50,60,70)
def maxdigit(x,y):
    if x>y:
        return x
    else:
        return y
x=new.reduce(maxdigit, mytuple)
print(x)    