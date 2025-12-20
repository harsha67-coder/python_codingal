l=[12,22,5,6]
l.sort()
print(l)
#median
if len(l)%2==0:
    median1=l[len(l)//2-1]

#mean(average)
sum=sum(l)
mean=sum/len(l)
print("value of median=",median1)
print("value of mean= ",mean)

