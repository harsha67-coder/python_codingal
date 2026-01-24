def add(a,b):
    return a+b
def sub(a,b):
    return a-b 
def div(a,b):
    return a/b 
def mul(a,b):
    return a*b
a=1
b=3
print("enter ur choise of operation here:")
print("1 add")
print("2 sub")
print("3 div")
print("4 mul")
choice=int(input("enter ur choice of operation here:"))
if choice==1:
    print(add(a,b))
if choice==2:
    print(sub(a,b))
if choice==3:
    print(div(a,b))
if choice==4:
    print(mul(a,b))
else:
    print()

