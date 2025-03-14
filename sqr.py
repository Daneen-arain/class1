import turtle


def draw_square():
    screen = turtle.Screen()
    screen.bgcolor("blue")
    
    pen = turtle.Turtle()
    pen.pensize(3)
    pen.speed(3)
    pen.color("pink")
    
    for _ in range(4):
        pen.forward(100)  # Move forward by 100 pixels
        pen.right(90)  # Turn right by 90 degrees
    
    pen.hideturtle()
    screen.mainloop()

# Call the function to draw a square
draw_square()
