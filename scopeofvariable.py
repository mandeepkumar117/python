x=10
def show():
    global y,z
    y=20
    x=40
    z=30
    print(y)
    print(x)
    print(globals()['x']) #globle scope value ko local scope value ko override karne ke liye globles function()['']
show()
print(x)
print(y)   
print(z) 