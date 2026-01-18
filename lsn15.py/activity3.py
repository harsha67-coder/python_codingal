import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(600,400)
t=turtle.Turtle()
t.penup()
t.goto(-100,0)
t.pendown()
for i in range(3):
    t.forward(150)
    t.left(120)
t.penup()
t.goto(-100,70)
t.pendown()
for i in range(3):
    t.forward(150)
    t.right(120)
input()