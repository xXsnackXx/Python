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
wn.register_shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukichair.gif")
wn.register_shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukibag.gif")


# Setting first yuki
cookie = turtle.Turtle()
cookie.shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukicookie.gif")
cookie.speed(0)

# Counter display
clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("pink")
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
    

    # Change Img at 50 clicks
    if clicks == 50:
        cookie.shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukicute.gif")
        

    # Change Img at 100 clicks
    if clicks == 100:
        cookie.shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukichair.gif")

    # Change Img at 150 clicks
    if clicks == 150:
        cookie.shape(r"C:\Users\Devon\Documents\GITREPOS\Python\CookieClicker\yukibag.gif")

    # Milestone 50 clicks message
    if clicks == 50:
        message.write("You got a new Yuki Pic!", align="center", font=("Beach", 24, "bold"))
        wn.ontimer(message.clear, 3000)

         # Milestone 100 clicks message
    if clicks == 100:
        message.write("Chair Yuki!", align="center", font=("Beach", 24, "bold"))
        wn.ontimer(message.clear, 3000)

        # Milestone 150 clicks message 
    if clicks == 150:
        message.write("Yuki got a bag upgrade!", align="center", font=("Beach", 24, "bold"))
        wn.ontimer(message.clear, 3000)

cookie.onclick(clicked)


wn.mainloop()