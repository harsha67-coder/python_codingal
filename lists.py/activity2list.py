length=int(input("enter the number of elemnts to enter here :"))
mylist=[]
for i in range(length):
    element=int(input("enter the elements here :"))
    mylist.append(element)

search=int(input("enetr the element to find the number of appearences in the list :"))
count=0
for i in mylist:
    if i==search:
        count=count+1
print(mylist)
print("the number of the specific element ",search,"appears",count,"times in the list")