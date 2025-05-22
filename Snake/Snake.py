# Simple Snake Game in Python 3 
# By @Voidland
# IMPORT---------------------
import turtle
import time
import subprocess
import os
import signal
import random
# IMPORT---------------------

music_proc = subprocess.Popen(["python", r"C:\Users\Devon\Documents\GITREPOS\Python\Snake\soundtest.py"],
    cwd=r"C:\Users\Devon\Documents\GITREPOS\Python\Snake")

delay = 0.15

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
head.color("#66CCFF")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []







# Functions
# Move change
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

# Move Speed
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Key Binding 
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Check for collison 
if head.distance(food) < 20:
     # Move the food random
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

            # Add a segment
    new_segment = turtle.Turtle
    new_segment.speed(0)
    new_segment.shape("circle")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

    # Move the end segments first in reverse order
for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        y = head.xcor()
        x = head.ycor()
        segments[0].goto(x, y)



# Main Game loop
try:
    while True:
        wn.update()

        move()
        
        time.sleep(delay)
except turtle.Terminator:
    pass
finally:
    # Cleanly stop the music when the game window is closed
    if music_proc.poll() is None:  # Still running
        music_proc.terminate()

wn.mainloop()
