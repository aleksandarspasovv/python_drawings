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

# Function to draw an octagon
def draw_octagon(side_length):
    for _ in range(8):
        t.forward(side_length)
        t.right(45)  # 360 / 8 = 45 degrees for an octagon

# Draw the pattern with expanding octagons and larger size
t.pendown()
side_length = 50
for x in range(num_colors):  # Number of octagons
    t.pencolor(rgb_to_hex(colors[x]))  # Set pen color to the current color
    draw_octagon(side_length)  # Draw an octagon
    t.left(12)  # Change the angle for the next octagon to create a pattern

    # Gradually increase the side length for expansion effect
    side_length += 1

    # Update the screen every 5 octagons to control the drawing speed
    if x % 5 == 0:
        screen.update()
        time.sleep(0.4)  # Add a longer delay

# Final update after drawing is complete
screen.update()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
