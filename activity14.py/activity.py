n=int(input("enter the number of times the pattern should appear"))
number=1
for i in range(n):
    for j in range(i+1):
        number+=1
        print(number," ",end="")
    print()
    

