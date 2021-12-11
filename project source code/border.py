from turtle import Turtle


class Border(Turtle):
    def __init__(self, corner, width, height):
        """
        Maintain Border object with a rectangular shape.
        Border class is a subclass of Turtle class.
        Initialize with corner, width,and height properties.
        """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.pensize(5)
        self.corner = corner
        self.height = height
        self.width = width

    @property
    def corner(self):
        """Takes in Border instance, return private attribute corner"""
        return self.__corner

    @corner.setter
    def corner(self, corner):
        """set a private attribute corner with corner"""
        self.__corner = corner

    @property
    def width(self):
        """Takes in Border instance, return private attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set a private attribute width with width"""
        self.__width = width

    @property
    def height(self):
        """Takes in Border instance, return private attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set a private attribute height with height"""
        self.__height = height

    def draw_border(self):
        """draw a border by using its corner, width, and height"""
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.pensize(5)
        self.penup()
        self.goto(self.corner[0], self.corner[1])
        self.pendown()
        self.goto(self.corner[0], self.height)
        self.goto(self.width, self.height)
        self.goto(self.width, self.corner[1])
        self.goto(self.corner[0], self.corner[1])

    def __repr__(self):
        """Take in Border instance, return a string"""
        return f'Border(corner={self.corner}, width={self.width}, height={self.height})'
