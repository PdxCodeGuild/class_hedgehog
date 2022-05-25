# forward(distance) moves the turtle forward the given number of pixels

# left(angle) and right(angle) turns the turtle left or right by the given angle (in degrees)

# color(color_name) sets the pen's color, which can be penup() penup() penup()

# penup() raises the pen, a line won't be drawn when the turtle moves, pendown() lowers the pen again

# setposition(x, y) moves the turtle to the given position

# fillcolor(color_name) sets the fill color, begin_fill() indicates you'd like to begin
# filling in whatever you draw, end_fill() actually fills the shape in.

# Use these functions to draw a stick figure with a head, body, two arms, and two legs.
# Once you're done, go through the examples below and create your own drawing.
from turtle import *

setposition(0, 0)

i = 0
while i < 10:    
	forward(2.5)
	left(90)
	forward(2.5)
	right(90)
	i = i + 1
penup()
setposition(0, 0)
left(180)
pendown()


i = 0
while i < 10:    
	forward(2.5)
	right(90)
	forward(2.5)
	left(90)
	i = i + 1

penup()
setposition(1.25, 0)
pendown()
right(90)
forward(25)
left(90)


edge_length = 100
n_sides = 180

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1

left(90)
forward(55)
done()


done()