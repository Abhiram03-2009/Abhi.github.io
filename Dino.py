# This program simulates the effect of gravity on a ball
import turtle

GRAVITY = -0.2
HEIGHT = 20

screen = turtle.Screen()
screen.title("Dino Game")
screen.setup(800, 600)

turtle.tracer(0)

#Create the turtles
lucy = turtle.Turtle()
dino = turtle.Turtle()
cactus = turtle.Turtle()

# Register the custom shapes in to the program
turtle.register_shape("dino.gif")
turtle.register_shape("cactus.gif")

def on_space_bar_key_press():
   print("Space bar has been pressed")
   current_y = dino.ycor()
   current_y = current_y + 100
   dino.sety(current_y)   
    
# Draw ground
lucy.pensize(4)
lucy.penup()
lucy.goto(-400, 0)
lucy.pendown()
lucy.goto(400, 0)
lucy.penup()
lucy.hideturtle()

score = 0
scorer = turtle.Turtle()
scorer.hideturtle()
scorer.penup()
scorer.goto(-100, 200)
scorer.write("Score:" + str(score), font = ("verdana", 24, "normal"))

# Set dino
dino.speed(0)
dino.shape("dino.gif")
dino.penup()
dino.goto(0, HEIGHT/2)

# Set cactus
cactus.shape("cactus.gif")
cactus.penup()
cactus.goto(320, HEIGHT/2)

screen.listen()
screen.onkeypress(on_space_bar_key_press, "space")

# Game loop
while True:
    current_y = dino.ycor()
    current_y = current_y + GRAVITY
    dino.sety(current_y)
    current_x = cactus.xcor()
    current_x = current_x - 0.2
    cactus.setx(current_x)
    
# Set the ball back to the ground level if it goes beyond the ground level
    if dino.ycor() < HEIGHT/2:
        dino.goto(-360, HEIGHT/2)
    
    if cactus.xcor() < -360:
        score = score + 1
        cactus.goto(320, HEIGHT/2)
    
    if dino.distance(cactus) <= 10:
        print("Game over")
        scorer.clear()
        scorer.write("Score:" + str(score) + ' ' + "Game over", font = ("verdana", 24, "normal"))
        break
    
    scorer.clear()
    scorer.write("Score:" + str(score), font = ("verdana", 24, "normal"))
    turtle.update()
    
turtle.mainloop()
