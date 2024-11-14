n=int(input("Enter row no:"))
i=0
while i<n:
    # print('*' * n)
    # print('*' * i + (n-1) * ' ')    
    # print((n-i) * '*' + ' ' * i)
    # print(' ' * i + '*' * (n-i))
    print(' ' * (n-i) + ' *' * i)
    i=i+1