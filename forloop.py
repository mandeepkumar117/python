# Q.1 print natureal number
# n=int(input("enter number:"))
# sum=0
# for i in range(1,n+1):
#     if i<=(n-1):
#         print(i,end="+")
#     else:
#         print(i,end="=") 
#     sum=sum+i
# print(sum) 

# Q2 print even number

# n=int(input("enter number:"))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+i
#         if i<=(n-2):
#             print(i,end="+")
#         else:
#             print(i,end="=")
# print(sum) 
# 
# 
# n=int(input("enter number:"))
# sum=0
# for i in range(1,n+1):
#     if i<n-1:
#         print(i*2,end=",")
#     else: 
#         print(i*2)   



# n=int(input("enter number:"))
# sum=0
# for i in range(1,n+1):
#     if i<n-1:
#         print((i*2)-1,end=",")
#     else:
#         print((i*2)-1)    
    

n=input("enter any string: ")
v=0
c=0
for i in n:
    x=['a','e','i','o','u','A','E','I','O','U']
    if i in x:
        v=v+1
        print(i)  
    else:
        c=c+1
        print(i)
print(v)
print(c)            