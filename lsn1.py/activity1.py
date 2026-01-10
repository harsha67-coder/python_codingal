text=input("enter ur text here :")
letter=input("enter the letter to be searched:")
count=0
length=len(text)
for i in range(0,length):
    if text[i]==letter:
        count=count+1
    
print(letter,"appears",count,"times")
