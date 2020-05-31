# Simple pong game in python

import turtle  # basic GUI module

window = turtle.Screen()
window.title('Pong by @ayushmann__01')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-375, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(375, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.goto(0, 0)
ball.penup()
ball.speed(0)
ball.dx = 0.1
ball.dy = 0.1


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# KeyBindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "x")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


# Main game loop

while True:
    window.update()

    # move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Border checking
    if ball.ycor() > 280:
        ball.sety(-285)
        ball.dy *= -1
    if ball.ycor() < -280:
        ball.sety(285)
        ball.dy *= -1
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1

