from turtle import Turtle
import math


class Player(Turtle):
    """
    Maintain Player object which movement can be controlled.
    Player class is a subclass of Turtle class.
    Initialize with name, colour, speed, is_alive, and score properties.
    """
    def __init__(self, name, color):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color(color)
        self.colour = color
        self.speed = 2.0
        self.name = name
        self.position = [0, 0]
        self.score = 0
        self.is_alive = True

    @property
    def name(self):
        """Takes in Player instance, return private attribute name"""
        return self.__name

    @name.setter
    def name(self, name):
        """set a private attribute name with name"""
        self.__name = name

    @property
    def colour(self):
        """Takes in Player instance, return private attribute colour"""
        return self.__colour

    @colour.setter
    def colour(self, colour):
        """set a private attribute colour with colour"""
        self.__colour = colour

    @property
    def speed(self, **kwargs):
        """Takes in Player instance, return private attribute speed"""
        return self.__speed

    @speed.setter
    def speed(self, speed):
        """set a private attribute speed with speed"""
        self.__speed = speed

    @property
    def position(self):
        """Takes in Player instance, return private attribute position"""
        return self.__position

    @position.setter
    def position(self, position):
        """set a private attribute position with position"""
        self.__position = position

    @property
    def is_alive(self):
        """Takes in Player instance, return private attribute is_alive"""
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        """set a private attribute is_alive with is_alive(Boolean)"""
        self.__is_alive = is_alive

    @property
    def score(self):
        """Takes in Player instance, return private attribute score"""
        return self.__score

    @score.setter
    def score(self, score):
        """set a private attribute score with score"""
        self.__score = score

    def __repr__(self):
        """Take in Player instance, return a string"""
        return f'Player(name={self.name}, color={self.color})'

    def move(self):
        """move the Player instance with its speed attribute"""
        self.forward(self.speed)
        # turn left when player hit the border
        if self.xcor() > 270 or self.xcor() < -270:
            self.left(60)
        if self.ycor() > 270 or self.ycor() < -270:
            self.left(60)
        # update position attribute
        self.position = [self.xcor(), self.ycor()]

    def turn_left(self):
        """move left 30 degree"""
        self.left(30)

    def turn_right(self):
        """move right 30 degree"""
        self.right(30)

    def is_collision_item(self, _item):
        """check if player hit the item or not"""
        a = self.xcor() - _item.xcor()
        b = self.ycor() - _item.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 20:
            return True
        else:
            return False

    def is_collision_obs(self, obstacle):
        """check if player hit the obstacle or not"""
        a = self.xcor() - obstacle.xcor()
        b = self.ycor() - obstacle.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 20:
            return True
        else:
            return False
