n=int(input("enter the number of elements on the list here :"))
list1=[]
for i in range(1,n+1):
    value=int(input("enter the values/elements here:"))
    list1.append(value)
print(list1)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)