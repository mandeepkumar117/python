# ex.1

# x=10
# class Student:
#     x=50
#     def add():
#         print(x)
#         x=20
#         print(x)
# obj=Student
# print(x)  
# obj.add
# print(x)  
# 
# 
# ex.2

# x = 50  

# class Student:
#     global x
#     x=10
#     def add(self):         
#         print(x)  
#         y = 20    
#         print(y) 
    
#     def add1(self):
#         print(x)
# obj = Student()  
# obj.add()        
# obj.add1()      
# print(x)


# ex.3
# x=40
# class School:
#     def add(self):
#         print(x)
# obj=School()
# obj.add()

# x=90
# class Student:
#     x=40
#     def add():
#         print(x)
#         y=10
#         print(x)
#     def add1():
#         print(x)    
# obj=Student
# obj.add()  
# obj.add1() 

x=50
def new():
    global x
    print(x)
    x=10
    print(x)
print(x)    
new() 
print(x)   