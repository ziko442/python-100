from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red','orange','yellow','green','blue','purple']
all_turtles = [] 
y = -75
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y)
    y += 33
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        

screen.exitonclick()





# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_left():
#     tim.setheading(tim.heading() + 10)

# def turn_right():
#     tim.setheading(tim.heading() - 10)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forwards,"w")
# screen.onkey(move_backwards,"s")
# screen.onkey(turn_left,"a")
# screen.onkey(turn_right,"d")
# screen.onkey(clear,"c")