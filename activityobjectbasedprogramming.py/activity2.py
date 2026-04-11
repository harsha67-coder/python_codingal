class Iostring():
    def __init__(self):
        self.str1=""

    def get_string(self):
       self.str1=input("unter the string here:")

    def print_string(self):
        uppercase=print("result :",self.str1.upper())

str1=Iostring()

str1.get_string()
str1.print_string()
    
