limit=int(input("enter the imit here :"))

for num in range(2,limit+1):
    prime="yes"
    for i in range(2,num):
        if num%i==0:
            print="no"
            break 
    if prime=="yes":
       print(num)


