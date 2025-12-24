units=int(input("enter the consumption of units here:"))
if units<=50:
    amount=units*2.6
    surcharge=25
elif units<=100:
    amount=130+((units-50)*3.25)
    surcharge=45
elif units <=200:
    amount=130+162.50+((units-100)*5.26)
    surcharge=75
else:
    amount=130+162.50+526+((units-200)*7.75)
    surcharge=100

total=surcharge+amount
print("the bill is MRP:",total)

   
          