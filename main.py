# Python game of pong

import turtle


def run_game():
    win = turtle.Screen()
    win.title('Pong game')
    win.bgcolor('white')
    win.setup(width=1000, height=750)
    # stop the window from automatically updating
    win.tracer(0)

    # Paddle 1
    paddle_1 = turtle.Turtle()
    # set speed to the maximum possible
    paddle_1.speed(0)
    paddle_1.shape('square')
    paddle_1.color('red')
    paddle_1.shapesize(stretch_wid=8, stretch_len=1)
    # no trail
    paddle_1.penup()
    paddle_1.goto(-460, 0)

    # Paddle 2
    paddle_2 = turtle.Turtle()
    # set speed to the maximum possible
    paddle_2.speed(0)
    paddle_2.shape('square')
    paddle_2.color('blue')
    paddle_2.shapesize(stretch_wid=8, stretch_len=1)
    # no trail
    paddle_2.penup()
    paddle_2.goto(460, 0)

    # Ball
    ball1 = turtle.Turtle()
    ball1.speed(0)
    ball1.shape('square')
    ball1.color('black')
    ball1.shapesize(stretch_wid=2, stretch_len=2)
    ball1.penup()
    ball1.goto(0, 0)
    # movement
    ball1.dx = 0.2
    ball1.dy = 0.2

    def paddle_1_up():
        y = paddle_1.ycor()
        y += 20
        paddle_1.sety(y)

    def paddle_1_down():
        y = paddle_1.ycor()
        y -= 20
        paddle_1.sety(y)

    def paddle_2_up():
        y = paddle_2.ycor()
        y += 20
        paddle_2.sety(y)

    def paddle_2_down():
        y = paddle_2.ycor()
        y -= 20
        paddle_2.sety(y)

    # keyboard binding
    win.listen()
    win.onkeypress(paddle_1_up, 'w')
    win.onkeypress(paddle_1_down, 's')
    win.onkeypress(paddle_2_up, 'Up')
    win.onkeypress(paddle_2_down, 'Down')

    # main loop
    while True:
        win.update()

        # ball movement
        ball1.setx(ball1.xcor() + ball1.dx)
        ball1.sety(ball1.ycor() + ball1.dy)

        # top/bottom - borders: 750/ 2 = 375 || ball1 = 40 ==> 375 - 20 = 355
        if ball1.ycor() > 355:
            ball1.sety(355)
            ball1.dy *= -1

        if ball1.ycor() < -355:
            ball1.sety(-355)
            ball1.dy *= -1

        # left/right - borders: 1000/ 2 = 500 || ball1 = 40 ==> 500 - 20 = 480
        if ball1.xcor() > 480:
            ball1.goto(0, 0)
            ball1.dx *= -1

        if ball1.xcor() < -480:
            ball1.goto(0, 0)
            ball1.dx *= -1

        # paddle reaction
        if (440 < ball1.xcor() < 450) and (paddle_2.ycor() + 95 > ball1.ycor() > paddle_2.ycor() - 85):
            ball1.setx(440)
            ball1.dx *= -1

        if (-450 < ball1.xcor() < -440) and (ball1.ycor() < paddle_1.ycor() + 95) \
                and (ball1.ycor() > paddle_1.ycor() - 85):
            ball1.setx(-440)
            ball1.dx *= -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()
