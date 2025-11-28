import turtle as t

screen = t.Screen()
screen.title("Turtle Trophy Game")
screen.bgcolor("#bfe2c6")
screen.setup(width=600, height=600)

player = t.Turtle()
player.shape("turtle")
player.color("#1b4538")
player.penup()
player.speed(0)
player.goto(-250, -250)

trophy = t.Turtle()
trophy.shape("circle")
trophy.color("#e2a854")
trophy.penup()
trophy.goto(200, 200)
trophy.shapesize(2, 2)

def up():
    player.setheading(90)
    player.forward(20)

def down():
    player.setheading(270)
    player.forward(20)

def left():
    player.setheading(180)
    player.forward(20)

def right():
    player.setheading(0)
    player.forward(20)

def check_win():
    if player.distance(trophy) < 30:
        player.hideturtle()
        trophy.hideturtle()

        win_text = t.Turtle()
        win_text.hideturtle()
        win_text.penup()
        win_text.goto(0, 0)
        win_text.write("You reached the trophy! 🎉", align="center",
                       font=("Arial", 24, "bold"))

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

while True:
    check_win()
    screen.update()
