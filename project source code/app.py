from turtle import Turtle, Screen
import json
from player import Player
from score import Score
from border import Border
from stage import Stage
import time


def app_mode():
    """show the introduction screen and ask for type of mode to perform"""
    interface = Screen()
    interface.register_shape('interface_wallpaper.gif')
    # show my project name and my name on the screen
    project_name = Turtle()
    interface.setup(width=400, height=400)
    interface.bgpic('interface_wallpaper.gif')
    interface.title('Basic Turtle Game')
    project_name.hideturtle()
    project_name.color('#8BF412')
    style = ('Courier', 15, 'italic')
    project_name.write(f'Welcome to my Turtle Game:\n<please set your mode>', font=style, align='center')
    project_name.penup()
    project_name.goto(150, -150)
    project_name.color('#E5FB07')
    project_name.write(f'Thank you\n<Supakrit65>', font=style, align='right')
    # Pop up a dialog window for input of app mode
    mode_choice = interface.textinput('App Mode', 'Type (p) to play a game or '
                                                  '(v) to view your score or (q) to quit: ').lower()
    # if input is invalid, ask for input again
    while mode_choice not in ['p', 'v', 'q']:
        # show a warning message on the screen for invalid input
        warning = Turtle()
        warning.hideturtle()
        warning.penup()
        warning.goto(-150, -80)
        warning.color('white')
        warning.write('Warning:\nPlease give a valid mode input', font=("Arial", 10, "normal"))
        mode_choice = interface.textinput('App Mode', 'Type (p) to play a game or '
                                                      '(v) to view your score or (q) to quit: ').lower()
        warning.clear()
    if mode_choice == 'p':
        # clear all the old messages
        project_name.clear()
        instruction = Turtle()
        instruction.hideturtle()
        instruction.penup()
        # call game_mode with instruction(a message on the screen) as argument
        game_mode(instruction)
    elif mode_choice == 'v':
        view_mode(interface, project_name)
    else:
        print('App Closed')


def game_mode(instruction):
    """Ask for specific input to create and maintain the game and save progress"""
    style = ('Courier', 12, 'italic')
    # write down game instruction
    instruction.goto(0, 0)
    instruction.color('white')
    instruction.write(f'Please input your username & color', font=style, align='center')
    instruction.goto(0, -150)
    style = ('Courier', 10, 'italic')
    instruction.color('#F7FE00')
    instruction.write(f'Game instruction:\nEat the items and avoid others turtle', font=style, align='center')
    # create a stage and border
    stage_corner = [-280, -280]
    stage_height = 280
    stage_width = 280
    border = Border(stage_corner, stage_height, stage_width)
    stage = Stage(border, Screen())
    # pop up dialog window for user input
    user_name, user_color = stage.ask_input()
    instruction.clear()
    # create player and items and obstacles on the screen
    player = Player(user_name, user_color)
    stage.create_screen(player)
    stage.add_item(8)
    stage.add_obs(4, player, False)
    # show your current score and the old high score
    score = Score()
    high_score = Score()
    # show your initial score which is 0
    score.update_score(player)
    high_score.show_high_score()
    delay_obs = 200   # delay loop for obstacle spawn
    delay_item = 300  # delay loop for item spawn
    delay_count_obs = 0
    delay_count_item = 0
    step = 1
    time_sleep = 0.0001
    hardest_level = Turtle()
    # start game loop
    while True:
        # update the screen
        stage.update_screen()
        player.move()
        for item in stage.items:
            item.move()
            # if player hit the item, item relocates randomly and your score increases
            if player.is_collision_item(item):
                item.jump()
                score.change_score(100, player)
        # add more obstacle every some period of time
        if delay_count_obs >= delay_obs:
            # limit max obstacles on screen to 8
            if len(stage.obstacles) < 8:
                stage.add_obs(1, player, True)
                delay_count_obs = 0
                delay_obs *= 1.5
                # increase hardest level if player manage to survive for a period of time
                if len(stage.obstacles) > 6:
                    stage.medium_mode(hardest_level)
                    step = 2
            else:
                # when screen hold max amount of obstacles, start hard mode
                hardest_level.clear()
                stage.hard_mode(hardest_level)
        # add more item on screen every some period of time
        if delay_count_item == delay_item:
            # limit max items on screen to 12
            if len(stage.items) < 12:
                stage.add_item(1)
                delay_count_item = 0
        for obs in stage.obstacles:
            obs.move()
            # end game if player hits the obstacle
            if player.is_collision_obs(obs):
                score.old_high_score = score.get_high_score()
                score.save_score(player)
                stage.end(score)
        delay_count_obs += step
        delay_count_item += 1
        # delay the screen update
        time.sleep(time_sleep)


def view_mode(screen, user_data):
    """ask for a username which user want to view information and show them"""
    screen.clearscreen()
    screen.setup(400, 400)
    instruction = Turtle()
    instruction.hideturtle()
    style = ('Courier', 15, 'italic')
    # show instruction message on the screen
    instruction.write('Please type your username\nyou what to view score', font=style, align='center')
    screen.bgcolor('#D8FA04')
    # pop up a dialog window for input for a username
    username = screen.textinput('View Mode', 'Please type your username you what to view score: ')
    instruction.clear()
    message = view_score(username)
    user_data.penup()
    user_data.goto(0, -70)
    user_data.pendown()
    user_data.color('black')
    # show the data of the given username
    user_data.write(f'Username: {username}\n{message}\n\n\nclick to exit the window',
                    font=("Calibri", 18, "bold"), align='center')
    screen.exitonclick()


def view_score(username):
    """return the user data from the json file"""
    try:
        with open('game_data.json', 'r') as data_file:
            data_dict = json.load(data_file)
    except FileNotFoundError:
        return f'No Data File Found'
    else:
        # check if given username is found on the json file
        if username in data_dict:
            color = data_dict[username]['color']
            your_score = data_dict[username]['score']
            return f'Color: {color}\nScore: {your_score}'
        else:
            return f'No details for {username} exists.'


# Main
app_mode()
