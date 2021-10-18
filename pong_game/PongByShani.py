
import turtle
import winsound


play = True

wn = turtle.Screen()
wn.title("Pong by Shani")
wn.bgcolor("light slate gray")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.bgpic("bg.gif")


# Scores
score_a = 0
score_b = 0
round_number = 1
winner = "Null"


# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("gray", "alice blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # so we won't draw a line on the screen
paddle_a.goto(-350, 0)  # where to start (at the screen)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("gray", "azure")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # so we won't draw a line on the screen
paddle_b.goto(+350, 0)  # where to start (at the screen)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("gray", "old lace")
ball.penup()  # so we won't draw a line on the screen
ball.goto(0, 0)  # where to start (at the screen)
# saparating the ball's movement into 2 parts - x and y movement
ball.dx = 0.2
ball.dy = 0.2

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()  # so we won't draw a line on the screen
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))


pen_2 = turtle.Turtle()
pen_2.speed(0)
pen_2.color("white")
pen_2.penup()  # so we won't draw a line on the screen
pen_2.hideturtle()
pen_2.goto(0, 220)
pen_2.write("Round number : {}/5".format(round_number), align="center",
            font=("Courier", 16, "normal"))

pen_3 = turtle.Turtle()
pen_3.speed(0)
pen_3.color("white")
pen_3.penup()  # so we won't draw a line on the screen
pen_3.hideturtle()


# Function for paddle a


def paddle_a_up():  # when 'w' is pressed (up key!) update y's cordinates (add 20) and set it as new paddle cordinates
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():  # when 's' is pressed (down key!) update y's cordinates (minus 20) and set it as new paddle cordinates
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Function for paddle b


def paddle_b_up():  # when 'w' is pressed (up key!) update y's cordinates (add 20) and set it as new paddle cordinates
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():  # when 's' is pressed (down key!) update y's cordinates (minus 20) and set it as new paddle cordinates
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()

# when w is pressed, go to 'paddle_a_up' function.
wn.onkeypress(paddle_a_up, "w")
# when w is pressed, go to 'paddle_a_down' function.
wn.onkeypress(paddle_a_down, "s")

# when w is pressed, go to 'paddle_b_up' function.
wn.onkeypress(paddle_b_up, "Up")
# when w is pressed, go to 'paddle_a_down' function.
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while play:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (screen width 800, height is 600 and the ball is 20) + increasing score
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("ground", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("ground", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.setx(390)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("win", winsound.SND_ASYNC)
        round_number += 1
        pen_2.clear()
        pen_2.write("Round number : {}/5".format(round_number),
                    align="center", font=("Courier", 16, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("win", winsound.SND_ASYNC)
        round_number += 1
        pen_2.clear()
        pen_2.write("Round number : {}/5".format(round_number),
                    align="center", font=("Courier", 16, "normal"))

    # Paddle and ball collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ball", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("ball", winsound.SND_ASYNC)

    if round_number == 6:
        play = False


winsound.PlaySound("finish", winsound.SND_ASYNC)
ball.hideturtle()
pen.hideturtle()
pen_2.hideturtle()
paddle_a.hideturtle()
paddle_b.hideturtle()
wn.clearscreen()
wn.bgpic("bg.gif")


if score_a > score_b:
    winner = "A"
else:
    winner = "B"

while not play:

    pen_3.goto(0, 0)
    pen_3.write("The winner is player {} !!".format(winner),
                align="center", font=("Courier", 30, "normal"))
