from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        self.move_speed *= 0.9
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_paddle()
