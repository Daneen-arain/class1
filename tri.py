import turtle

turtle.Screen().bgcolor("light blue")
turtle.Screen().setup(300, 300)

polygon = turtle.Turtle()

num_sides = 3
side_length = 100
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.color('red')
    polygon.forward(side_length)
    polygon.left(angle)

turtle.done()
