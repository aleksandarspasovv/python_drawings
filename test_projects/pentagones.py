import turtle
import colorsys
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color to black
screen.setup(width=800, height=800)  # Set up a wider square window

# Set up the turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)  # Set the turtle speed to the fastest value

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

# Function to draw a pentagon
def draw_pentagon(side_length):
    for _ in range(5):
        t.forward(side_length)
        t.right(72)  # 360 / 5 = 72 degrees for a pentagon

# Draw the pattern with expanding pentagons and larger size
t.pendown()
side_length = 50
for x in range(num_colors):  # Number of pentagons
    t.pencolor(rgb_to_hex(colors[x]))  # Set pen color to the current color
    draw_pentagon(side_length)  # Draw a pentagon
    t.left(12)  # Change the angle for the next pentagon to create a pattern

    # Gradually increase the side length for expansion effect
    side_length += 1

    # Update the screen every 5 pentagons to control the drawing speed
    if x % 5 == 0:
        screen.update()
        time.sleep(0.2)  # Add a longer delay

# Final update after drawing is complete
screen.update()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
