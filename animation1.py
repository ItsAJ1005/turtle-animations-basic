import colorsys
import turtle


t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor('black')

# Set the drawing speed of the turtle to the maximum
t.speed(0)

# Define the number of iterations and initialize the hue
n = 36
h = 0

for i in range(460):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    # Increment the hue for the next iteration
    h += 1/n
    t.color(c)
    
    # Rotate the turtle left by 145 degrees
    t.left(145)

    for j in range(5):
        t.forward(300)
        t.left(150)

# Keep the window open
turtle.done()
