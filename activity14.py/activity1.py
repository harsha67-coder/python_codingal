n=int(input("enter the number of times for the pattern to appear"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()