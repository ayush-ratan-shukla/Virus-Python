import turtle
a=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('Black')
a.color('cyan')
a.speed(0)
a.hideturtle()
for x in range(200):
    a.forward(x)
    a.left(x-1)
turtle.done()