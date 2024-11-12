=int(input("Enter any range: "))
i=1
sum=0
while i<=n:
    if i%2==0:
        if i<n-1:
            print(i,end=",")
        else:
            print(i)  
        sum=sum+i          
    i=i+1 
print("total even number of sum= ",sum) 
                   