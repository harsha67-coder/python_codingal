x = input("Enter something: ")


if x.isdigit():
    print("You entered a number")


elif x.isalpha():
    print("You entered alphabets")


elif "." in x:
    print("You entered a float number")

else:
    print("You entered something else")