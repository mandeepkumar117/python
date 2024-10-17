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
        #  (Reference)  variable      |
        #                             |                    "apple" adress is 736
        #                             |                          
        #                             |                     20 addres is 080
        #   fruit addres is 656       |
        #                             |                      100 addres is 640
        #                             |                  ______________ 
        #                             |                 |736| 080| 640|
        #                             |                 |___|____|____|
        #                             |               656

# fruit=("apple",20,100)
# print(type(fruit))
# # fruit[2]=200 #tuple immutable
# print(id(fruit))
# print(id(fruit[0]),id(fruit[1]),id(fruit[2]))
# fruit=("apple",20,100)+("banana",9999)
# print(fruit)
# fruit=("apple",20,99)
# print(fruit)

# number=(34,45)+(56,90)
# number=number + (89,90)
# print(number)

# q)
lis=[["ajay","mandeep"],(23,45)]
# print(type(lis[1]))
# lis[1][0]=89
# print(lis)
# lis.pop()
# print(lis)

# q.2)
# t=(34,55,[3,4,555])
# print(t)
# t[2][1]=987
# print(t)
# t[2].append(456)
# print(t)

# q.3)
# lis=[["ajay","aman"],(45,[87,67])]
# lis[1][1][0]=56
# print(lis)
# lis[1][1].append(23)
# print(lis)

#len() #max(), #min(), #sum(), #index(), #count()
# t=(3,4,5,6,7,3)
# a=t.count(3)
# print(a)
# a=sorted(t)
# print(a)



t=(23,)
print(type(t))
t1=("fofgjo",)
print(type(t1))

t2=1,2,34,5,67 # use in function
print(type(t2))
