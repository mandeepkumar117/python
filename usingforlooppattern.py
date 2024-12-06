# *
# **
# ***
# ****
# *****
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print("*"*i + (n-i) * " ")


# *
# * *
# * * *
# * * * *
# * * * * *
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print("* "*i + (n-i) * " ")


# *
# **
# ***
# ****
# *****
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i)

#      *
#     ***
#    *****
#   *******
#  *********
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*(2*i-1))


#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i)," *"*i)

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()  


# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


#  *****
#   ****
#    ***
#     **
#      *
# n=int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     print(" "*(n-i),"*"*i)

# *****
# ****
# ***
# **
# *
# n=int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     print("*"*i)

#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
# n=int(input("Enter the number of rows: "))
# for i in range(n,0,-1):
#     print(" "*(n-i)," *"*i)

#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     print(" "*(n-i),"* "*i)
# m=n-1
# for i in range(m,0,-1):
#     print(" "*(m-i)," *"*i)

#      *
#     **
#    ***
#   ****
#  *****
# *****
# ****
# ***
# **
# *

# n=int(input("Enter the number of rows: "))
# for i in range(0,n+1):
#     print(" "*(n-i),"*"*i)
# for i in range(n,0,-1):
#     print("*"*i," "*(n-i))

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# n=int(input("Enter the number of rows: "))
# for i in range(0,n+1):
#     print("* "*i)
# m=n-1
# for i in range(m,0,-1):
#     print("* "*i)

#      *
#     **
#    ***
#   ****
#  *****
#  *****
#   ****
#    ***
#     **
#      *

n=int(input("Enter the number of rows: "))
for i in range(0,n+1):
    print(" "*(n-i),"*"*i)
for i in range(n,0,-1):
    print(" "*(n-i),"*"*i)




