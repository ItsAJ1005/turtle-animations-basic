import turtle
import colorsys

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')

# Set the drawing speed
t.speed(0)


def draw_spiral():
    for i in range(360):
        # Convert angle to hue value
        hue = i / 360.0
        # Convert hue to RGB color
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        # Set the turtle color
        t.color(color)
        
        # Draw a line and rotate the turtle
        t.forward(i)
        t.right(45)

# Move the turtle to a starting position
t.penup()
t.goto(0, 0)
t.pendown()

# Call the function to draw the spiral
draw_spiral()

# Keep the window open
turtle.done()
