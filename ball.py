import turtle
import random

class Manager:
    def __init__(self) -> None:
        pass


class Ball:
    def __init__(self):
        canvas_width = turtle.screensize()[0]
        canvas_height = turtle.screensize()[1]
        ball_radius = 0.05 * canvas_width
        turtle.colormode(255)

        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.size = ball_radius
        self.xpos = random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius)
        self.ypos = random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius)
        self.vx = random.randint(1, 0.01*canvas_width)
        self.vy = random.randint(1, 0.01*canvas_height)
        
    def draw_circle(self, color, size, x, y):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move_circle(self):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        
        self.xpos += self.vx
        self.ypos += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (self.canvas_width - self.ball_radius):
            self.vx = -self.vx

    # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (self.canvas_height - self.ball_radius):
            self.vy = -self.vy
