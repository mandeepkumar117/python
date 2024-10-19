# emty list->
# 1)
# lis=[]
# 2)
# li=list()#list method
# print(lis)
# print(li) 

#any() this is method

# print(any(lis))
# lis=[67]
# print(any(lis))

# append->add element in the last element
 
# lis=[23,34,45,5,6]
# print(lis)
# lis.append(20)
# print(lis)

# lis=[["mango", "banana"],["200/kg", "50/dozen"]]
# lis[0].append("apple")
# lis[1].append("300/kg")
# print(lis)

# extend->accept sequnce data 

# lis=[["mango", "banana"],["200/kg", "50/dozen"]]
# lis.extend(["pineapple","arange"])
# print(lis)



# insert->where you want to add data.then we have to use insert function

# insert(index,element)
# lis=["mango", "banana"]
# print(lis)
# lis.insert(1,"apple")
# print(lis)
# lis[1]="guavas"
# print(lis)

# lis=["mango", "banana","90"]
# lis1=[23,4,6,77,98]
# m=max(lis1)
# print(m)
# m=max(lis)
# print(m)
# m=len(lis)
# print(m)
# m=len(lis1)
# print(m)
# m=min(lis)
# print(m)
# m=sum(lis1)
# print(m)


# lis1=[23,4,6,77,98,89,89,97]
# m=lis1.index(97)
# print(m)
# m=lis1.count(89)
# print(m)


# lis1=["ajay", "mandeep", "aditya","aditya","sourabh", "aditya"]
# print(lis1)
# lis1.reverse()
# print(lis1)
# # deleted_value=lis1.pop()
# # print(lis1)
# # print(deleted_value)

# lis1.remove("aditya")
# lis1.remove("aditya")
# lis1.remove("aditya")

# print(lis1)
# del lis1
# print(lis1)
# lis1.clear()
# print(lis1)

# slice method->slice is not a method
# lis1[start: end: jump]
# jump->default 1
# : >colon by defoult start 0. only starting index colon
# end->exclude(just brfor end)
lis1=[12,34,35,'sourabh',56,5,8,'aditya',33,56,9]
# a=lis1[3:8:1]
# print(a)
# b=lis1[3:8:1]
# print(b)
# print(lis1)
# a=lis1[3:]
# print(a)
# a=lis1[3::7]
# print(a)
# a=lis1[3:7]+lis1[8:]
# print(a)
# a=lis1[7:2:-1]
# print(a)
# a=lis1[-4:-9:-2]
# print(a)
a=lis1[::-1]
print(a)


# st="we are here to learn python. and slicing is very helpfull"
# a=st[7:21:]
# print(a)
# a=st[33:57:]
# print(a)
# a=st[3:19:3]
# print(a)
# a=st[:21]+"cpp"+st[27:]
# print(a)