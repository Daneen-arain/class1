import turtle  # importing library

turtle.Screen().bgcolor("light blue")
turtle.Screen().setup(300, 300)

polygon = turtle.Turtle()  # defined variable

num_sides=int(input ('enter number or sides:'))
side_length=70
angle=360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)
    polygon.color('red')

turtle.done()
