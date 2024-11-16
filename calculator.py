while True:
    # print("1.Add\n 2.subtract\n 3.multiplication\n 4.divide\n 5.OFF")
    n=int(input("Enter your choice: "))
    x=[1,2,3,4]
    if n in x:
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        if n==1:
            print("Adition = ",x+y)
        elif n==2:
            print("subtraction = ", x-y)
        elif n==3:
            print("multiplication = ",x*y)
        elif n==4:
            print("divide = ",x/y)
    elif n==5:
        break
    else:
        print("please enter right number thank you")                   