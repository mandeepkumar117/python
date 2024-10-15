# tuple->
# 0)it is container,which store multiple data oblect
# 1)it is sequnce data type.(order data type)
# 2)it is a immutable data type
#3) a)representation ()
# b)comma seprated
# 4)it is faster then list
# 5)single element representation
# 6)generally whenever data is fetched from database it is stored in the from of tuple or dictionary
  
# note->



        # stack                       |                     heap(object)
        #   Reference                 |
        #   variable                  |                    "apple" adress is 736
        #                             |                          
        #                             |                     20 addres is 080
        #   fruit addres is 656       |
        #                             |                      100 addres os 640
        #                             |                  ______________ 
        #                             |                 |736| 080| 640|
        #                             |                 |___|____|____|
        #                             |               656

fruit=("apple",20,100)
print(type(fruit))
# fruit[2]=200 #tuple immutable
print(id(fruit))
print(id(fruit[0]),id(fruit[1]),id(fruit[2]))
fruit=("apple",20,100)+("banana",9999)
print(fruit)
fruit=("apple",20,99)
print(fruit)
# fruit=99999999
# print(fruit)
