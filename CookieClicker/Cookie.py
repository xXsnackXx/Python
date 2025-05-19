# Cookie Clicker Game
# By @Voidland

import turtle
import winsound

turtle.bgpic(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\pxfuel.png")

wn = turtle.Screen()
wn.title("Yuki Clicker by @VoidLand")
wn.bgcolor("black")
wn.setup(width=600, height=600)

# Yuki pic shape register 

wn.register_shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukicookie.gif")
wn.register_shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukicute.gif")

cookie = turtle.Turtle()
cookie.shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukicookie.gif")
cookie.speed(0)

# Counter display
clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 150)
pen.write(f"Clicks: {clicks}", align="center", font=("Beach", 32))

# Milestone message turtle 
message = turtle.Turtle()
message.hideturtle()
message.color("cyan")
message.penup()
message.goto(0, -200)

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Beach", 32, "normal"))
    winsound.PlaySound(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukiclicksound.wav", winsound.SND_ASYNC)

    # Change Img at 100 clicks
    if clicks == 5:
        cookie.shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukicute.gif")

    # Milestone 50 clicks message
    if clicks == 5:
        message.write("You got a new Yuki Pic!", align="center", font=("Beach", 24, "bold"))

cookie.onclick(clicked)



wn.mainloop()