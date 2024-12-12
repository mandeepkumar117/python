# Declaration of instance variable
# 1)inside class
# *)through constructor
# *)through instance method
# 2)outside class
# *)through object

# calling of instance variable
# 1)inside class
# *)used self
# *)used object


class Student:
    def __init__(self,name,age):
        self.name=name #declaration of instance variable
        self.age=age   #declaration of instance variable
        print(self.name) #calling of instance variable
    def add(self,school):
        self.school=school  #declaration of instance variable
    def show_detail(self):
        print(self.name) #calling of instance variable
        print(self.age)  #calling of instance variable
        print(self.school) #calling of instance variable
        print(self.city)
obj=Student("mandeep",26) 
obj.add('shsc')   
print(obj.name)    
obj.city="bhopal"
obj.show_detail()       