import turtle

no_sides=int(input("enter the no.of sides here:"))
length=int(input("enter the length here:"))
def draw_shape(length,no_sides):
    """this function is used to draw shapes.it is very useful aswell"""
    for i in range(0,no_sides):
        turtle.forward(length)
        turtle.right(360/no_sides)

draw_shape(length,no_sides)
input("test")