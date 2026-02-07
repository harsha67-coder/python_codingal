def num_input(message):
    while True:
        try:
            value_num=int(input(message))
            return value_num
        except ValueError:
            print("value error pls enter proper value")
        except:
            print("error occured ,pls try again")
num1=num_input("enter the first number here:")
num2=num_input("enter the second number here :")
ans=("the addition of both values are:",num1+num2)
            
