from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        """require one parameter : choose 1 for position (x=350 and y=0),
         or 2  for position (x=-350 and y=0)"""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        if position == 1:
            self.setposition(350, 0)
        if position == 2:
            self.setposition(-350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def check_limit(self):
        if self.ycor() < -250:
            self.goto(self.xcor(), self.ycor() + 20)
         
        if self.ycor() > 250:
            self.goto(self.xcor(), self.ycor() - 20)

            
            