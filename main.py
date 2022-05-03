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
    ball1.shape('circle')
    ball1.color('black')
    ball1.shapesize(stretch_wid=2, stretch_len=2)
    ball1.penup()
    ball1.goto(0, 0)

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()
