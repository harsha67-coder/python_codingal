import turtle


def draw_number(length,no_side=4):
    for i in range(0,no_side):
        turtle.right(360/no_side)
        turtle.forward (length)

draw_number(50,4)
draw_number(50,5)
draw_number(50,6)
input("test")
