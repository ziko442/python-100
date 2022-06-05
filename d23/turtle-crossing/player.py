from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.go_to_start()
        self.setheading(90)
        self.showturtle()

    # def move(self):
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def check_wall_limit(self):
        if self.xcor() < -280:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())
        elif self.xcor() > 280:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

        if self.ycor() < -280:
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)


