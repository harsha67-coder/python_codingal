def square():
    list2=[]
    list1=[]
    
    for i in range(3):
        num=int(input("enter 3 random numbers to find their sqaures"))
        list1.append(num)
    for j in list1:
        multy=j**2
        list2.append(multy)
    print(list2)
    for i in list2:
        if i%2==0:
            print("even square present",i)
        else:
            print("odd square num",i)
square()

    



