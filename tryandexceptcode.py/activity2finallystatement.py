try:
    num1,num2=eval(input(("enter 2 numbers seperated by commas here :")))
    result=num1/num2
    print(result)


except zerodevisionerror:
    print("u cannot divide zero with any number!!!")
except syntaxerror:
    print("there is no comma here ,pls enter  properly")
except:
    print("wrong input")
finally:
    print("this code will run no matter what")
