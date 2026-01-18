import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(600,400)
t=turtle.Turtle()
no_sides=int(input("enter the number of sides here :"))
for i in range(no_sides):
    t.forward(100)
    t.left(360/no_sides)
input()