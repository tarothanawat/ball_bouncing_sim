import turtle
from ball import Ball

num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()

balls = []

for i in range(num_balls):
    ball = Ball()
    balls.append(ball)


while (True):
    turtle.clear()
    for ball in balls:
        ball.draw_circle(ball.color, ball.size, ball.xpos, ball.ypos)
        ball.move_circle()
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
