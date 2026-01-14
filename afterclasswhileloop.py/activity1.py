r=0
user=int(input("enter the number to see it's binary form :"))
binary_num=""
q=user
while(q>=1) or (q==user):
    r=int(q%2)
    q=int(q/2)
    binary_num = binary_num+str(r)
    #print(r)
print(binary_num[::-1])#slicing
 