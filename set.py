# set:- set is a contaianer in which we contain multiple data, but duplication  is not allowed, and unordered data type
# where our main concern  is data, but not any ordder related to it,then we use set

          
# a={1,3,9,7,2,5,9}
# b={2,3,99,11.99}
# a^b={3,2,5}
# a u b={1,7,9,3,2,5,99,11}
# a-b={1,7,9}
# b-a={11,99}

# a u b u c={33}
# a^ b ^ c={2}


# s1={1,2,3,4,3,9,11,17}
# s2={5,4,9,17,89}
# s3={"a,","b", 1,2,3,88}
# r=s1.difference(s2)
# print(r)
# r=s1-s2
# print(r)
# r=s2-s1
# print(r)
# s1.union(s2)
# print(s1)
# s1.update(s2)
# print(s1)
# s1.add(344)
# print(s1)
# s1.add((2,90,99))
# print(s1)
# s1.add((2,90))
# print(s1)


s = {10,'20','Rahul', 234.56, True}
print(s)
print(type(s))