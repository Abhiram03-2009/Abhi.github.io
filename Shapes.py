# This program draws a design

import turtle

import tkinter as tk

writer = turtle.Turtle()
my_turtle = turtle.Turtle(shape = "turtle")

WIDTH = 720
HEIGHT = 360

def setup():
  screen = turtle.Screen()
  screen.setup(WIDTH, HEIGHT)
  screen.title("Shapes")
  screen.bgcolor("Black")
  writer.penup()
  writer.hideturtle()
  writer.goto(-200,10)
  writer.showturtle()

setup()

def square():
  writer.color("blue")
  writer.pendown()
  writer.forward(100)
  writer.right(90)
  writer.color("red")
  writer.pendown()
  writer.forward(100)
  writer.right(90)
  writer.color("yellow")
  writer.pendown()
  writer.forward(100)
  writer.right(90)
  writer.color("green")
  writer.pendown()
  writer.forward(100)
  writer.right(90)

def circle():
    r = 100
    writer.circle(r)

def button_square():
  screen = turtle.Screen()
  screen.bgcolor("black")
  button_1 = tk.Tk()
  button_1.geometry("200x100")
  canvas = screen.getcanvas()
  a = tk.Button(button_1, text = "Square", text_color = "White", command = square)
  canvas.create_window(-200, -200, window=a)
  a.pack()
  button_1.mainloop()

button_square()
  
def button_circle():
  button_2 = tk.Tk()
  button_2.geometry("200x100")
  b = tk.Button(button_2, text = "Circle", command = circle)
  b.pack()
  button_2.mainloop()
  
button_circle()

def button_triangle():
  button_3 = tk.Tk()
  button_3.geometry("200x100")
  c = tk.Button(button_3, text = "Triangle")
  c.pack()
  button_3.mainloop()
  
button_triangle()

def button_rectangle():
  button_4 = tk.Tk()
  button_4.geometry("200x100")
  d = tk.Button(button_4, text = "Rectangle")
  d.pack()
  button_4.mainloop()

button_rectangle()
    
turtle.mainloop()
