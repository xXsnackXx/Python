# Simple Snake Game in Python 3 
# By @Voidland

import turtle
import time

delay = 0.1

turtle.bgpic(r"C:\Users\Devon\Documents\GITREPOS\Python\Snake\animesnakebg.png")


# Set up Screen 

wn = turtle.Screen()
wn.title("Snake Game by @Voidland")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#00FF00")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

# Main Game loop
# while True:
    wn.update()

    move()

    time.sleep(delay)

    






wn.mainloop()
