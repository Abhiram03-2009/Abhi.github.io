# This program creates 3 Turtles and makes them race towards a finish line.

import turtle
import random

# Create all of the variables
LINE_LENGTH = 200
LINE_WIDTH = 8
FINISH_POS_Y = 235
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
HEADING_NORTH = 90
RACER_PEN_SIZE = 3
RAND_MIN = 1
RAND_MAX = 5

def screen_setup():
  
# Set the screen width and height.
    canvas = turtle.Screen()
    canvas.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

def organize_track():
  
# The organizer is responsible for drawing the race track details.
    organizer = turtle.Turtle()
    organizer.hideturtle()
    organizer.pensize(LINE_WIDTH)

# Draw the finish line.
    organizer.penup()
    organizer.goto(-100, 240)
    organizer.pendown()
    organizer.forward(LINE_LENGTH)
    
organize_track()

def create_racers():
  
# Create racer #1 - lucy.
    lucy = turtle.Turtle()

# Prepare the racer by setting the color, shape, and pensize.
    lucy.shape('turtle')
    lucy.color('red')
    lucy.pensize(RACER_PEN_SIZE)

# Move the racer to the starting position without leaving a trail.
    lucy.penup()
    lucy.goto(-90, -235)
    lucy.pendown()

# Make the racer face north.
    lucy.setheading(HEADING_NORTH)

# Create racer #2 - leo. 
    leo = turtle.Turtle()

# Prepare the racer by setting the color, shape, and pensize.
    leo.shape('turtle')
    leo.color('blue')
    leo.pensize(RACER_PEN_SIZE)

# Move the racer to the starting position without leaving a trail.
    leo.penup()
    leo.goto(90, -235)
    leo.pendown()

# Make the racer face north.
    leo.setheading(HEADING_NORTH)

# Create racer #3 - mike. 
    mike = turtle.Turtle()

# Prepare the racer by setting the color, shape, and pensize.
    mike.shape('turtle')
    mike.color('green')
    mike.pensize(RACER_PEN_SIZE)

# Move the racer to the starting position without leaving a trail.
    mike.penup()
    mike.goto(0, -235)
    mike.pendown()

# Make the racer face north.
    mike.setheading(HEADING_NORTH)

    create_racers()

def race_movement():

# Begin the race.
    while True:
  # Move forward the racers by a random number of pixels.
      lucy.forward(random.randint(RAND_MIN, RAND_MAX))
      leo.forward(random.randint(RAND_MIN, RAND_MAX))
      mike.forward(random.randint(RAND_MIN, RAND_MAX))
  
  # End the race if one of the racer's reach the finish line. 

race_movement()

turtle.mainloop()
