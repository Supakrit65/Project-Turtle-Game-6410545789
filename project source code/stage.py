from turtle import Turtle
from obstacle import Obstacle
from item import Item
import random
import math


class Stage(Turtle):
    """
    Represent a stage for all objects such as border and a screen, as well
    as a Player object, Item object, Obstacle objects.
    Stage class is a subclass of Turtle class.
    Stage class provides many important methods for the game.
    """
    def __init__(self, border, screen):
        super().__init__()
        self.border = border
        self.screen = screen
        # contain list of items and obstacles
        self.items = []
        self.obstacles = []

    @property
    def border(self):
        """Takes in Stage instance, return private attribute border"""
        return self.__border

    @border.setter
    def border(self, border):
        """set a private attribute border with border"""
        self.__border = border

    @property
    def screen(self):
        """Takes in Stage instance, return private attribute screen"""
        return self.__screen

    @screen.setter
    def screen(self, screen):
        """set a private attribute screen with screen"""
        self.__screen = screen

    @property
    def items(self):
        """Takes in Stage instance, return private attribute items"""
        return self.__items

    @items.setter
    def items(self, items):
        """set a private attribute items with items"""
        self.__items = items

    @property
    def obstacles(self):
        """Takes in Stage instance, return private attribute obstacles"""
        return self.__obstacles

    @obstacles.setter
    def obstacles(self, obstacles):
        """set a private attribute obstacles with obstacles"""
        self.__obstacles = obstacles

    def create_screen(self, player):
        """maintain a interactive screen with a title and a wallpaper"""
        # create GUI screen
        self.show_title()
        self.screen.bgcolor('#F0CBCC')
        self.screen.title('Simple Turtle GUI Game by Supakrit')
        self.screen.setup(width=660, height=660)
        self.screen.bgpic('sWallper.gif')
        self.screen.register_shape('item.gif')
        # update screen manually
        self.screen.tracer(0)
        # create border
        self.border.draw_border()
        # listens for screen input such as left and Right keys
        self.screen.listen()
        self.screen.onkey(fun=player.turn_left, key='Left')
        self.screen.onkey(fun=player.turn_right, key='Right')

    def ask_input(self):
        """Pop up a dialog window for input of a username and color, and return them"""
        user_name = self.screen.textinput(title='Make your decision', prompt='Username of player: ')
        user_color = self.screen.textinput(title='Make your decision',
                                           prompt='Pick your player\'s color '
                                                  '(cyan, yellow, green, pink, violet) : ').lower()
        # repetitively ask for another input if user give a invalid input
        while user_color not in ['yellow', 'cyan', 'green', 'pink', 'violet']:
            print('Please choose valid color choice.')
            user_color = self.screen.textinput(title='Make your decision', prompt='Pick your player\'s color (blue, '
                                                                                  'yellow, green) : ').lower()
        return user_name, user_color

    def update_screen(self):
        """update the screen which is a class property"""
        self.screen.update()

    def add_item(self, n):
        """add item to its items list for n times"""
        for i in range(n):
            self.items.append(Item())

    def add_obs(self, n, player, late):
        """add obstacle to its obstacles list for n time"""
        born_location_list = [[-200, -200], [-100, 100], [220, 100], [-150, 250],
                         [100, -150], [150, 200], [0, -180]]
        for i in range(n):
            # obstacle will have a random born location on the screen
            born_location = [random.randint(-270, 270), random.randint(-270, 270)]
            if late:
                while True:
                    # calculate obstacle distance from the player
                    a = player.xcor() - born_location[0]
                    b = player.ycor() - born_location[1]
                    distance = math.sqrt((a ** 2) + (b ** 2))
                    # make sure that obstacle do not instantly spawn too close to player
                    if distance < 60 or distance > 160:
                        born_location = [random.randint(-270, 270), random.randint(-270, 270)]
                    else:
                        break
                self.obstacles.append(Obstacle(born_location))
            # run else for the first time
            else:
                self.obstacles.append(Obstacle(random.choice(born_location_list)))

    @staticmethod
    def show_title():
        """show game title on the screen"""
        title = Turtle()
        title.penup()
        title.hideturtle()
        title.speed(0)
        title.color('#203EE7')
        title.goto(-85,293)
        title.write(f'Feast of the Turtle', False,
                    font=("Verdana", 15, 'bold'))

    def medium_mode(self, mode_text):
        """increase the speed of obstacles and display 'medium mode' on the screen"""
        mode_text.hideturtle()
        for obs in self.obstacles:
            obs.speed = 2
        mode_text.penup()
        mode_text.goto(180, -311)
        mode_text.color('#700815')
        mode_text.write(f'Medium Mode', font=("Verdana", 12, 'bold'), align='center')

    def hard_mode(self, mode_text):
        """increase the speed of obstacles and display 'hard mode' on the screen"""
        mode_text.hideturtle()
        for obs in self.obstacles:
            obs.speed = 3
        mode_text.penup()
        mode_text.goto(180, -311)
        mode_text.color('#700815')
        mode_text.write(f'Hard Mode', font=("Verdana", 12, 'bold'), align='center')

    def end(self, score):
        """display your score on the screen"""
        text = Turtle()
        # clear the old screen
        self.screen.clear()
        Stage.show_title()
        self.screen.bgcolor('#F0CBCC')
        self.screen.title('Simple Turtle GUI Game by Supakrit')
        self.screen.setup(width=660, height=660)
        self.screen.bgpic('sWallper.gif')
        # show the high score on the top of the screen
        score.show_high_score()
        text.penup()
        text.hideturtle()
        text.color('#8CF310')
        text.goto(0, 0)
        style = ('Courier', 30, 'italic')
        # check if player break the previous high score
        if score.score > score.old_high_score:
            text.goto(0, -50)
            text.write(f'Game over:\nYou got a HIGH SCORE!\n\n'
                       f'Your score is {score.score}', font=style, align='center')
        else:
            text.write(f'Game over:\n\n'
                       f'Your score is {score.score}', font=style, align='center')
        text.goto(80, -270)
        end_style = ("Verdana",12, "normal")
        text.write('click the screen to exit', font=end_style)
        self.screen.exitonclick()
