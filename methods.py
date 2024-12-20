# 1)instance method
# 2)class methods
# 3)static methods
# ex:-
# 1)istance methods->there is  must be first parameter


# class A:
#     def new(self):
#         print("1 st  method")
#     def new1(self):
#         self.new()
#         print("2nd method")

# obj=A()
# # obj.new()
# obj.new1()


# 2)class method->to chnge value of static methods then we use class method

class Book:
    price=150
    def __init__(self,author,pages):
        self.author=author
        self.pages=pages
    @classmethod
    def update_price(ds,price):
        ds.price=price
    def show_detail(self):
        print(self.author)    
        print(self.pages)    
        print(Book.price)    
obj=Book("mandeep",540)
obj.show_detail()
obj.update_price(200)
obj.show_detail()

        