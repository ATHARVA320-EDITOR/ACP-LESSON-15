import turtle
turtle.Screen().bgcolor("yellow")
polygon = turtle.Turtle()
num_sides = 4
side_legth = 90
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_legth)
    polygon.right(angle)
turtle.done()
