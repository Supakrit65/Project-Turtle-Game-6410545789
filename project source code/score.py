from turtle import Turtle
import json


class Score(Turtle):
    """
    Maintain Score object which can track your score and save it.
    Score class is a subclass of Turtle class.
    Initialize with score property and old_high_score attribute.
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('#900C3F')
        self.score = 0
        self.old_high_score = 0

    @property
    def score(self):
        """Takes in Score instance, return private attribute score"""
        return self.__score

    @score.setter
    def score(self, score):
        """set a private attribute score to score"""
        self.__score = score

    def show_high_score(self):
        """get high score from get_high_score method and show it on the screen"""
        high_score = self.get_high_score()
        self.goto(270, 290)
        self.write(f'High score: {high_score}', False, align='right', font=("Comic Sans MS", 12, "normal"))

    @staticmethod
    def get_high_score():
        """extract data from json file and return a int of high score """
        try:
            with open('game_data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            return 0
        else:
            scores = []
            for each_dict in data.values():
                scores.append(each_dict['score'])
            high_score = max(scores)
            return int(high_score)

    def update_score(self, player):
        """update the current score of the player"""
        self.clear()
        self.goto(-280, 290)
        self.write(f'Score: {self.score}', False, align='left', font=("Comic Sans MS", 14, "normal"))
        # update player score
        player.score = self.score

    def change_score(self, points, player):
        """update score property and call update_score function"""
        self.score += points
        self.update_score(player)

    @staticmethod
    def save_score(player):
        """at the end of the game save username, color, and score on json file"""
        # create new_data dict storing username as key and color and score as value
        new_data = {
            player.name: {
                'color': player.colour,
                'score': player.score
            }
        }
        try:
            with open('game_data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('game_data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('game_data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
