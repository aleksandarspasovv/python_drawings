import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color to black
screen.setup(width=800, height=800)  # Set up a wider square window

# Set up the turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)  # Set the turtle speed to the maximum

# Generate 300 different colors
num_colors = 300
colors = []
for i in range(num_colors):
    hue = i / num_colors
    lightness = 0.5
    saturation = 1
    rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
    colors.append((rgb[0], rgb[1], rgb[2]))


# Convert RGB to turtle-compatible format
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))


# Turn off screen updates for faster drawing
screen.tracer(0)

# Draw the pattern with expanding ellipses and larger size
t.pendown()
radius = 100
small_radius = 20
for x in range(num_colors):  # Number of ellipses
    t.pencolor(rgb_to_hex(colors[x]))  # Set pen color to the current color
    t.circle(radius, 70)  # Main ellipse radius
    if x % 2 == 0:
        t.circle(small_radius, 70)  # Smaller ellipse radius

    # Gradually increase the radius for expansion effect
    radius += 1
    small_radius += 0.1

# Update the screen after drawing is complete
screen.tracer(1)
screen.update()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
