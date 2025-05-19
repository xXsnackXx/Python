# Cookie Clicker Game
# By @Voidland

import turtle
import winsound 

wn = turtle.Screen()
wn.title("Yuki Clicker by @VoidLand")
wn.bgcolor("black")
wn.setup(width=600, height=600)

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
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
    winsound.PlaySound(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukiclicksound.wav", winsound.SND_ASYNC)

    # Change Img at 100 clicks
    if clicks == 50:
        cookie.shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukicute.gif")

cookie.onclick(clicked)



wn.mainloop()