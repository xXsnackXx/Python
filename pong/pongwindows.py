# Simple Pong in Python 3 for Beginners
# By @voidland


import turtle
import winsound 

wn = turtle.Screen()
wn.title("pong by @voidland")
wn.bgcolor("black")
wn.setup(width=800, height=640)
wn.tracer(0)

line_drawerb = turtle.Turtle()
line_drawerb.color("white")
line_drawerb.pensize(3)

# Move to start position without drawing
line_drawerb.penup()
line_drawerb.goto(-1000, -300)  # Starting point (x, y)
line_drawerb.pendown()



# Draw the horizontal line
line_drawerb.forward(2000)  # Length of line

line_drawera = turtle.Turtle()
line_drawera.color("white")
line_drawera.pensize(3)

# Move to start position without drawing
line_drawera.penup()
line_drawera.goto(-1000, 300)  # Starting point (x, y)
line_drawera.pendown()



# Draw the horizontal line
line_drawera.forward(2000)  # Length of line

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("pink")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = .09
ball.dy = .09

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
# Paddle A

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Paddle B

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



    # Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound(r"C:\Users\Devon\Documents\GITREPOS\Python\pong\pongwallsound.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound(r"C:\Users\Devon\Documents\GITREPOS\Python\pong\pongwallsound.wav", winsound.SND_ASYNC)

        # point logic update

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound(r"C:\Users\Devon\Documents\GITREPOS\Python\pong\pongpointsound2.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound(r"C:\Users\Devon\Documents\GITREPOS\Python\pong\pongpointsound2.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350  and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(r"C:\Users\Devon\Documents\GITREPOS\Python\pong\pongpaddlesound.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350  and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(r"C:\Users\Devon\Documents\GITREPOS\Python\pong\pongpaddlesound.wav", winsound.SND_ASYNC)