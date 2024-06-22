import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color to black

# Set up the turtle
t = turtle.Turtle()
t.hideturtle()
t.pencolor("white")  # Set the pen color to white

# Draw the pattern with expanding ellipses and larger size
t.pendown()
radius = 100
small_radius = 20
for x in range(300):  # Increase the number of iterations to draw more lines
    t.circle(radius, 70)  # Main circle radius
    if x % 2 == 0:
        t.circle(small_radius, 70)  # Smaller circle radius

    # Gradually increase the radius for expansion effect
    radius += 1
    small_radius += 0.1

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
