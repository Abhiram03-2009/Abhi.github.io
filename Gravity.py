# This program simulates the effect of gravity on a ball
import turtle

GRAVITY = -0.2
HEIGHT = 20

screen = turtle.Screen()
screen.title("Jumping Ball")
screen.setup(800, 600)

turtle.tracer(0)

def on_space_bar_key_press():
   print("Space bar has been pressed")
   current_y = jumper.ycor()
   current_y = current_y + 100
   jumper.sety(current_y)   
    
# Draw ground
pen = turtle.Turtle()
pen.pensize(4)
pen.penup()
pen.goto(-400, 0)
pen.pendown()
pen.goto(400, 0)
pen.penup()
pen.hideturtle()

score = 0
scorer = turtle.Turtle()
scorer.hideturtle()
scorer.penup()
scorer.goto(-100, 200)
scorer.write("Score:" + str(score), font = ("verdana", 24, "normal"))

# Set jumper
jumper = turtle.Turtle()
jumper.speed(0)
jumper.shape("circle")
jumper.color("red")
jumper.penup()
jumper.goto(0, HEIGHT/2)

screen.listen()
screen.onkeypress(on_space_bar_key_press, "space")

cactus = turtle.Turtle()
cactus.shape("square")
cactus.penup()
cactus.goto(320, HEIGHT/2)

# Game loop
while True:
    current_y = jumper.ycor()
    current_y = current_y + GRAVITY
    jumper.sety(current_y)
    
    current_x = cactus.xcor()
    current_x = current_x - 0.2
    cactus.setx(current_x)
    
# Set the ball back to the ground level if it goes beyond the ground level
    if jumper.ycor() < HEIGHT/2:
        jumper.goto(-360, HEIGHT/2)
    
    if cactus.xcor() < -360:
        score = score + 1
        cactus.goto(320, HEIGHT/2)
    
    if jumper.distance(cactus) <= 10:
        print("Game over")
        scorer.clear()
        scorer.write("Score:" + str(score) + ' ' + "Game over", font = ("verdana", 24, "normal"))
        break
    
    scorer.clear()
    scorer.write("Score:" + str(score), font = ("verdana", 24, "normal"))
    turtle.update()
    
turtle.mainloop()
