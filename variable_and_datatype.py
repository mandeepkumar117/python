# variables->variable is a reference to memory location where our object(data) resides.


num1=90
num2=100
num3=90
print(id(num1),id(num2),id(num3))
num1=98
print(id(num1),id(num2),id(num3))