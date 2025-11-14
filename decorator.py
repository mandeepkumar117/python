# Decorator एक function है जो किसी दूसरे function को modify करता है बिना उसकी actual code को बदले।

def outer_function(sanju):
    def inner_function(x,y):
        x=x+y
        y=y+x
        data=sanju(x,y)    
        return data
    return inner_function
@outer_function
def main_function(x,y):
    z=x+y
    return z
result=main_function(5,3)
print(result)


# import time

# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print("Execution time:", end - start)
#     return wrapper

# @timer
# def test():
#     for i in range(1000000):
#         pass

# test()
