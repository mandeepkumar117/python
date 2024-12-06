from functools import reduce
# import functools #both are gives same result


# syntax:
# x=lambda x: x**2
# print(x(5))


# example:

# x=lambda x,y,z,p,q,r:x+y-z/p%q//r
# print(x(1,2,3,4,5,6))
# q.1)find even number and also square  and square of sum 


# mylist=[10,15,34,20,50,40]
# even_data=filter(lambda x: x % 2 == 0,mylist)
# print(even_data)
# squnce_even=list(map(lambda x: x**2,even_data))
# print(squnce_even)
# squence_sum=reduce(lambda x,y:x+y,squnce_even)
# print(squence_sum)
# if you use direct funtools .you heve to use funtools.reduce

# z=functools.reduce(lambda x,y: x+y,x)
# print(z)
# q.2)find even number and also sum and sum of square
# mylist=[30,20,34,32,23,11,25]
# even_data=list(filter(lambda x: x%2==0,mylist))
# print(even_data)
# even_sum=reduce(lambda x,y: x+y,even_data)
# print(even_sum)
# # 1-------
# # even_square= even_sum**2
# # 2-----
# # even_square= lambda x:x**2
# # print(even_square(even_sum)) 


mylist=[30,20,34,32,23,11,25]
even_data=list(filter(lambda x: x%2==0,mylist))

even_sum=reduce(lambda x,y: x+y,even_data)

even_square= lambda even_sum: print(even_sum**2)
print(even_square)
