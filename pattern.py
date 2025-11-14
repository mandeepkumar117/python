# pattern print

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# for i in range(1, 5+1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# 1 
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for i in range(1,5+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()



# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3
# 1 2
# 1
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()    


# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()    



#     5 
#    4 5 
#   3 4 5
#  2 3 4 5
# 1 2 3 4 5
# for i in range(5,0,-1):
#     print(" "*(i-1),end="")
#     for j in range(i,5+1):
#         print(j,end=" ")
#     print()   



# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3
# 5 4
# 5
# for i in range(0,5):
#     for j in range(5,i,-1):
#         print(j,end=" ")
#     print() 

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3
# 4 4
# 5
# for i in range(1,5+1):
#     for j in range(5,i-1,-1):
#         print(i,end=" ")
#     print()  

# a 
# a b 
# a b c
# a b c d
# a b c d e
# for i in range(5):
#     for j in range(i+1):
#         print(chr(97+j),end=" ")
#     print()  

# a 
# b b 
# c c c
# d d d d
# e e e e e
# for i in range(5):
#     for j in range(i+1):
#         print(chr(97+i),end=" ")
#     print() 

#         * 
#       * * 
#     * * *
#   * * * *
# * * * * *
# for i in range(1,5+1):
#     print(" "*(5-i)*2,end="")
#     print("* " * i)



# *
# **
# ***
# ****
# *****
# for i in range(1,5+1):
#     print("*" * i)

# * * * * * 
# * * * * 
# * * *
# * *
# *
# for i in range(5,0,-1):
#     print("* " * i)