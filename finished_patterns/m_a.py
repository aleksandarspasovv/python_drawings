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

# Function to draw the letter "M"
def draw_m(t, size):
    t.pendown()
    t.left(90)
    t.forward(size)
    t.right(135)
    t.forward(size / 1.414)  # size / sqrt(2) for 45-degree angle
    t.left(90)
    t.forward(size / 1.414)  # size / sqrt(2) for 45-degree angle
    t.right(135)
    t.forward(size)
    t.penup()
    t.right(90)
    t.forward(size / 2)

# Function to draw the letter "A"
def draw_a(t, size):
    t.pendown()
    t.left(75)
    t.forward(size)
    t.right(150)
    t.forward(size)
    t.backward(size / 2)
    t.right(105)
    t.forward(size / 3)
    t.penup()
    t.left(75)
    t.forward(size / 2)

# Function to draw the letter "L"
def draw_l(t, size):
    t.pendown()
    t.left(90)
    t.forward(size)
    t.backward(size)
    t.right(90)
    t.forward(size / 2)
    t.penup()
    t.forward(size / 2)

# Function to draw the word "MAL"
def draw_mal(t, size):
    draw_m(t, size)
    draw_a(t, size)
    draw_l(t, size)

# Draw the pattern with the word "MAL" in a spiral pattern
size = 20
angle = 10  # The angle to turn after each "MAL"
for x in range(num_colors):  # Number of "MAL"
    t.pencolor(rgb_to_hex(colors[x]))  # Set pen color to the current color
    draw_mal(t, size)  # Draw "MAL" with current size
    t.right(angle)  # Turn right by the specified angle

    # Gradually increase the size for expansion effect
    size += 1
    t.forward(10)  # Move forward to avoid overlapping

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
