def show(**keyword):
    print(keyword)
    for i,j in keyword.items():
        print(i, "=",j)
show(name="mandeep", age=26, qualification="B.tech")        