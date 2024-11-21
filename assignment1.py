# 1. Write a program to check if a given number is an Armstrong
# number.(153=1**3+5**3+3**3)

# n=int(input("Enter any number: "))
# temp=n
# last=0
# sum=0
# while n>0:
#     last=n%10
#     sum=sum+last*last*last
#     n=n//10
# if temp==sum:
#     print("no is armstrong")
# else:
#     print("no is not armstrong")        

# 2. Write a program to check if the given string is a palindrome. (madam=madam)

# str=input("Enter any character: ")
# temp=str
# reverse=str[::-1]
# if(temp==reverse):
#     print("given string is palindrom: ")
# else:
#     print("not palindrom")        

# 3. Write a program to get the Fibonacci series. (0,1,1,2,3,5,8,13,21……………..)

# n=int(input("Enter any number: "))
# n1=0
# n2=1
# n3=0
# print(n1, n2,end= " ")
# for i  in range(n-2):
#     n3=n1+n2
#     print(n3,end=" ")
#     n1=n2
#     n2=n3


# 4. Write a program to find the factorial of a given number.    

# num=int(input("Enter a number: "))
# if num<0:
#     print("factorial is not defined for negative number.", end=" ")
# factorial=1
# for i in range(1, num+1):
#     if i<num:
#         print(i,end="*")
#     else:
#         print(i,end="=")    
#     factorial=factorial*i
# print(factorial) 

# 11.Write a program to check given number is Peterson number or not. ( A number is said
# to be a Peterson number if the sum of factorials of each digit of the number is equal to the
# number itself. Example – n=145, sum of 1!+4!+5!=145)


# n=int(input("Enter any number: "))
# temp=n
# sumoffactorial=0
# last=0
# while temp > 0:
#     last = temp % 10
#     fact=18
#     while last > 0:
#         fact = fact * last 
#         last = last-1  
#     sumoffactorial += fact
#     temp = temp // 10
# print(sumoffactorial)    
# if sumoffactorial == n:
#     print(n," is a peterson number")
# else:
#     print(n," is not a peterson number")






# 12.Write a program to check given number is spy no or not. ( A number is said to be a Spy
# number if the sum of all the digits is equal to the product of all digits. Examples: Input :
# 1412. 1+4+1+2 == 1*4*1*2 Output : Spy Number.)

# n=int(input("Enter any number: "))
# temp=n
# originalsum=0
# last=0
# while temp > 0:
#     last=temp % 10
#     originalsum  = originalsum + last
#     temp= temp//10
# print(originalsum)
# sumofsquare=1  
# temp=n
# while temp > 0:
#     digit= temp %10
#     sumofsquare = sumofsquare  * digit
#     temp=temp//10
# print(sumofsquare)  
# if originalsum == sumofsquare:
#     print(n,"is a spy number",end=" ")
# else:
#     print(n, "is not spy number")       


# 13.Write a program to check given number is sunny no or not. ( It is a positive number
# where the sum of its digits equals the number itself when those digits are squared.
# Example, 19 is a sunny number because 1**2 + 9**2 = = 82, now 8+2==1+9.)

# n=int(input("Enter any number: "))
# temp=n
# originalsum=0
# while temp>0:
#     originalsum=originalsum + temp % 10
#     temp=temp//10
# print(originalsum)
# sumofsquare=0
# temp=n
# while temp>0:
#     digit=temp % 10
#     sumofsquare=sumofsquare + digit * digit
#     temp=temp //10
# print(sumofsquare)

# reducedsum=0
# while sumofsquare > 0:
#     reducedsum = reducedsum + sumofsquare % 10
#     sumofsquare = sumofsquare //10
#     if sumofsquare == 0 and reducedsum >10:
#         sumofsquare = reducedsum
#         reducedsum =0
# print(reducedsum)

# if reducedsum == originalsum:
#     print(n,"is sunny number.",end=" ")
# else:
#     print(n, "is not a sunny number")            




  
