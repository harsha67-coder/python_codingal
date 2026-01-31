n=int(input("enter the number of names in the list here:"))
name_list=[]
for i in range(1,n+1):
    value=input("enter thr names here :")
    name_list.append(value)
print(name_list)
for i in name_list:
    if i[0]=="a" or i[0]=="A":
        print(i)
    