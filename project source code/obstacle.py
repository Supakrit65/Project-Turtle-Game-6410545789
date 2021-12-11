from turtle import Turtle
import random


class Obstacle(Turtle):
    """
    Maintain Obstacle object which move randomly.
    Obstacle class is a subclass of Turtle class.
    Initialize with speed and position properties.
    """
    def __init__(self, born_location):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('turtle')
        self.speed = 1.0
        # random the spawn location of obstacle across the screen
        self.goto(born_location)
        self.setheading(random.randint(0, 360))
        self.position = [self.xcor(), self.ycor()]

    @property
    def speed(self, **kwargs):
        """Takes in Obstacle instance, return private attribute speed"""
        return self.__speed

    @speed.setter
    def speed(self, speed):
        """set a private attribute speed with speed"""
        self.__speed = speed

    @property
    def position(self):
        """Takes in Obstacle instance, return private attribute position"""
        return self.__position

    @position.setter
    def position(self, position):
        """set a private attribute position with position"""
        self.__position = position

    def move(self):
        """move the Obstacle instance with its speed attribute"""
        # Obstacle instance has a circular moving pattern
        self.forward(self.speed)
        self.left(0.5)
        # turn left when obstacle hit the border
        if self.xcor() > 270 or self.xcor() < -270:
            self.left(60)
        if self.ycor() > 270 or self.ycor() < -270:
            self.left(60)
        # update position property
        self.position = [self.xcor(), self.ycor()]

    def __repr__(self):
        """Take in Obstacle instance, return a string"""
        return f'Obstacle(born_location={self.position})'
