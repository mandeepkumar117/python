# string:-

# 1)sequnce (order)
# 2)immutable

# msg="string is a immutable data type"
# print(msg[12:21])
# msg[3]="y"


# method of string:-

# msg="apple is good for helth"
# capitalize() -->return capitalize string
# a=msg.capitalize()
# print(a)

#upper() return upper case latter
# b=msg.upper()
# print(b)

# lower()-->return lower case latter
# c=msg.lower()
# print(c)

# d=msg.isupper()
# print(d)
# d=msg.islower()
# print(d)
# d=msg.isalnum()
# print(d)
# d=msg.isalpha()
# print(d)
# d=msg.isascii()
# print(d)
# d=msg.isdigit()
# print(d)
# d=msg.isnumeric()
# print(d)



# replace(old value,new value)

# s="we are here to learn c++ , it is a high level lang."


# s1=s.replace("c++", "python")
# print(s1)
# s2=s.replace('a','b',2)
# print(s2)

# s3=s.replace(s,"new")
# print(s3)



# split() return value is list
s="we are here to learn c++ , it is here a high level lang."


# s1=s.split()
# print(s1)

s1=s.split('e')
print(s1)
# s1=s.split("here")
# print(s1)
# s1=s.split("here",1)
# print(s1)


# join()return string

# lis=["apple","banana","pineapple","orange"]
# print(s)

# lis2=["graps","mango","guava"]

# s=", ".join(lis)+", "+", ".join(lis2)
# print(s)


# s="its now or never"
# s1="sti.won.ro.reven"

# s=s.split()
# print(s)
# a=s[0][::-1]
# b=s[1][::-1]
# c=s[2][::-1]
# d=s[3][::-1]
# s=[a,b,c,d]
# s=".".join(s)
# print(s)

# slice()

# s="apple banana"
# a=s[:6]
# print(a)
# b=s[::1]
# print(b)
# c=s[6:]+" "+s[:5]
# print(c)
