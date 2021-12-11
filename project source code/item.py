from turtle import Turtle
import random


class Item(Turtle):
    """
    Maintain Item object which move randomly.
    Item class is a subclass of Turtle class.
    Initialize with speed and position properties.
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('item.gif')
        self.speed = 0.5
        # random the spawn location of item across the screen
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
        self.setheading(random.randint(0, 360))
        self.position = [self.xcor(), self.ycor()]

    @property
    def speed(self, **kwargs):
        """Takes in Item instance, return private attribute speed"""
        return self.__speed

    @speed.setter
    def speed(self, speed):
        """set a private attribute speed with speed"""
        self.__speed = speed

    @property
    def position(self):
        """Takes in Item instance, return private attribute position"""
        return self.__position

    @position.setter
    def position(self, position):
        """set a private attribute position with position"""
        self.__position = position

    def jump(self):
        """teleport randomly on the screen and update a position property"""
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
        self.setheading(random.randint(0, 360))
        self.position = [self.xcor(), self.ycor()]

    def move(self):
        """move the Item instance with its speed attribute"""
        self.forward(self.speed)
        # turn left when item hit the border
        if self.xcor() > 270 or self.xcor() < -270:
            self.left(60)
        if self.ycor() > 270 or self.ycor() < -270:
            self.left(60)
        # update position property
        self.position = [self.xcor(), self.ycor()]

    def __str__(self):
        """Take in Item instance, return a string"""
        return 'Item moving with 0.5 speed and having a random position'
