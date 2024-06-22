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
screen.tracer(10)


# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        t.forward(size)
        t.left(120)


# Draw the pattern with expanding triangles and larger size
t.pendown()
size = 50
for x in range(num_colors):  # Number of triangles
    t.pencolor(rgb_to_hex(colors[x]))  # Set pen color to the current color
    draw_triangle(size)  # Draw a triangle
    t.left(12)  # Change the angle for the next triangle to create a pattern

    # Gradually increase the size for expansion effect
    size += 1

# Update the screen after drawing is complete
screen.tracer(1)
screen.update()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
