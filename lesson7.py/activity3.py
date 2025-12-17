math=float(input("enter ur math marks here:"))
if math>100:
    print("invalid mark")
sci=float(input("enter ur science marks here:"))
if math>100:
    print("invalid mark")
PE=float(input("enter ur PE marks here:"))
if math>100:
    print("invalid mark")
english=float(input("enter ur english marks here:"))
if math>100:
    print("invalid mark")
tamil=float(input("enter ur tamil marks here:"))
if math>100:
    print("invalid mark")
total =(math+sci+PE+english+tamil)/500
percent=total*100
print("your total percent is :",total*100)
if percent>=90:
    print("grade a")
elif percent>=80:
    print("grade b")
elif percent>=70:
    print("grade c")
elif percent>=60:
    print("grade d")
elif percent>=50:
    print("grade e")
else:
    print("grade f")
