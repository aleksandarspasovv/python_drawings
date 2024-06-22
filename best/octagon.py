import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color to black
screen.setup(width=800, height=800)  # Set up a wider square window

# Set up the turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)  # Set the turtle speed to the fastest

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

# Function to draw an octagon
def draw_octagon(t, size):
    for _ in range(8):
        t.forward(size)
        t.right(45)

# Draw the pattern with octagons in a spiral pattern
t.pendown()
size = 20
angle = 10  # The angle to turn after each octagon
for x in range(num_colors):  # Number of octagons
    t.pencolor(rgb_to_hex(colors[x]))  # Set pen color to the current color
    draw_octagon(t, size)  # Draw octagon with current size
    t.right(angle)  # Turn right by the specified angle

    # Gradually increase the size for expansion effect
    size += 1

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
