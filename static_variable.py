# static variable->aisa variable jo object ke badalne per value ko change na karen


# declaration->
# 1)inside class->
# a)outside method
# b)inside constructor
# c)inside instance method
# 2)outside class

class School:
    School_name="ergre"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        School.city='bhopal'
        print(self.name)
        print(self.age)
        print("callinh instance of constructor=",School.School_name)
    def add(self):
            School.code=101
            print(School.code)    
    def show_detail(self):
        #   print(School.code) # we can not leave empty block. so we have to deaclare pass
        #    print("hello")  
            pass     
School.greed="10th"
obj=School("mandeep",26)
obj.add() 
# print(School.code)
obj.show_detail()           

