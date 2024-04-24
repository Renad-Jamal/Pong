# Simple Pong in Python 3


import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong by RJ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # This is the speed of animation not the speed that the paddle moves on the screen
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,
                   stretch_len=1)  # the default shape is 20 pixels x 20 pixels, so I multiplied the width by 5 the length is set to 1 as the default
paddle_a.penup()  # Turtles draw a line as they're moving, and we don't need that
paddle_a.goto(-350, 0)  # This is where I want the paddle to start

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,
                   stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # I want to start in the middle of the screen

# Separate the ball's movement into 2. An X movement and a Y movement.
# d stands for delta or change
ball.dx = 0.1  # x is positive so the ball moves to the right by 2 pixels
ball.dy = -0.1  # y is positive so the ball moves up and diagonally by 2 pixels

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center", font=("Courier", 18, "normal"))


# Function (Using the keyboard I want to move Paddle A up and move Paddle A down, move Paddle B up and move Paddle B down)
def paddle_a_up():  # Here I defined the function
    y = paddle_a.ycor()  # To move the paddle I need to know the current y coordinate. This method returns the current y coordinate.
    y += 20  # Add 20 pixels to the y coordinate (I want to go up on the screen and y increases as we go up, so we add 20 pixels to the y coordinate)
    paddle_a.sety(y)  # After having calculated the y's it is now set to the new y coordinate


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20  # Instead of adding 20 subtract 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding       (Now we have to call the function)
wn.listen()  # This tells it to listen to keyboard input.
wn.onkeypress(paddle_a_up,
              "w")  # When the user presses w, call the function paddle_a_up (which calculates the current y coordinate, adds 20 and sets the new coordinate)
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()  # Every time the loop runs it updates the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (top and bottom borders)

    # since the ball is 20 high and 20 wide we're going to split the difference. Remember, the window height is 600, so that's 300 up and -300 down.

    if ball.ycor() > 290:
        ball.sety(290)  # send it back to 290
        ball.dy *= -1  # This reverses the direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Border checking (left and right borders, width 800)

    if ball.xcor() > 390:  # if it goes past the paddle and off the screen
        ball.goto(0, 0)  # send the ball back to the center
        ball.dx *= -1  # and reverse direction
        score_a += 1  # then gets a score
        pen.clear()  # and clears the previous score
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
