import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(600,400)
t=turtle.Turtle()
for i in range(3):
    t.forward(100)#pixels
    t.left(180/3)#degrees
input()