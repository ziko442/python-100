from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

# tim.shape("turtle")
# tim.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed('fastest')
angle = 6


def draw_spirograph(angle):
    for _ in range((360 // angle)):
        tim.circle(100)
        tim.right(angle)
        tim.color(random_color())


draw_spirograph(8)

screen = Screen()
screen.exitonclick()
