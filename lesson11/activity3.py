num=int(input("enter a number here :"))
original_num=num
length=len(str(num))
sum=0
while num>0:
    sum=sum+(num%10)**length
    num = num//10
if sum == original_num:
    print("it is an amstrong number")
else:
    print("not an amstrong number")

