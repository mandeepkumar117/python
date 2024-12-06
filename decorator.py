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