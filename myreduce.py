from functools import reduce

mytuple=(10,20,30,40,50,60,70)
def maxdigit(x,y):
    if x>y:
        return x
    else:
        return y
x=reduce(maxdigit, mytuple)
print(x)