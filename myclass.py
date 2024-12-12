
# self is a reference varibale  that hold current class of current object
# class Student:
#     "Student Information"
#     name='mandeep'
#     age=26
#     def __init__(self):
#         print(id(self))
#         print("constructor called........")
#     def add(p,q):
#         return p+q
# print(dir(Student))  
# print(Student.__doc__)
# print(Student.__dict__)
# obj=Student()
# print(id(obj))
# obj=Student
# print(obj.name)  
# print(obj.age)
# a=obj.add(2,3)
# print(a)



# ex-2.

class Student:
    "Student Information"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_detail(self):
            print(self.name)
            print(self.age)
    
    

obj=Student("mandeep",26)
obj.show_detail() 
   