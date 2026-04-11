class Employee:
    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructor called")

print("making object")
obj=Employee()
print("function end")
print("program end")