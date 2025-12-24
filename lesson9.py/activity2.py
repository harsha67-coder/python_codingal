medical_cause=input("do u have a medical cause (Y/N):")
att=int(input("pls type ur attendence down here :"))
if medical_cause=="Y" :
    if att>=60:
        print("u r allowed")
    else: 
        print("u r not allowed")
else:
    print("invalid input")
