from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock Paper Scissors")

# Variables
player_score = 0
computer_score = 0
global computer_points, player_points, game_text, weapons


class Img:
    """ Class responsible for displaying images. """
    def __init__(self):
        # Load images.
        self.question_img = Image.open("images/questionmark.png")
        self.rock_img = Image.open("images/rock.png")
        self.paper_img = Image.open("images/paper.png")
        self.scissors_img = Image.open("images/scissors.png")
        # Create PhotoImage objects from PIL images.
        self.question_photo = ImageTk.PhotoImage(self.question_img)
        self.rock_photo = ImageTk.PhotoImage(self.rock_img)
        self.paper_photo = ImageTk.PhotoImage(self.paper_img)
        self.scissors_photo = ImageTk.PhotoImage(self.scissors_img)
        # Resize of images.
        self.rock_small_photo, self.paper_small_photo, self.scissors_small_photo = self.resize_image(self.rock_img,
                                                                                                     self.paper_img,
                                                                                                     self.scissors_img)
        self.player_img = None
        self.computer_img = None

    def resize_image(self, rock_image, paper_image, scissors_image):
        # Resize images for weapon select.
        small_size = (100, 100)
        rock_small = rock_image.resize(small_size)
        rock_small_photo = ImageTk.PhotoImage(rock_small)
        paper_small = paper_image.resize(small_size)
        paper_small_photo = ImageTk.PhotoImage(paper_small)
        scissors_small = scissors_image.resize(small_size)
        scissors_small_photo = ImageTk.PhotoImage(scissors_small)
        return rock_small_photo, paper_small_photo, scissors_small_photo

    def create_players_img(self, mainframe):
        # Images below points.
        self.player_img = ttk.Label(mainframe, image=self.question_photo)
        self.player_img.grid(column=1, row=3)
        self.computer_img = ttk.Label(mainframe, image=self.question_photo)
        self.computer_img.grid(column=3, row=3)

    def computer_img_replace(self, image):
        # Changes the image of the computer's weapons.
        if image == 'rock':
            self.computer_img.configure(image=self.rock_photo)
        elif image == 'paper':
            self.computer_img.configure(image=self.paper_photo)
        elif image == 'scissors':
            self.computer_img.configure(image=self.scissors_photo)

    def select_weapon(self):
        # Updates player image when weapon is selected
        if weapons.get() == 'rock':
            img.player_img.configure(image=img.rock_photo)
        elif weapons.get() == 'paper':
            img.player_img.configure(image=img.paper_photo)
        elif weapons.get() == 'scissors':
            img.player_img.configure(image=img.scissors_photo)


img = Img()


class Game:
    """ Class responsible for game logic. """

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.choices = ['rock', 'paper', 'scissors']

    def start(self):
        """ Start the game by pressing the fight button. """
        computer_choice = random.choice(self.choices)
        if weapons.get() == "":
            game_text.configure(text='Please select your weapon!')
        else:
            img.computer_img_replace(computer_choice)
            if weapons.get() == computer_choice:
                game_text.configure(text='DRAW! There is no winner!')
            elif (weapons.get() == 'rock' and computer_choice == 'scissors') or \
                    (weapons.get() == 'paper' and computer_choice == 'rock') or \
                    (weapons.get() == 'scissors' and computer_choice == 'paper'):
                game_text.configure(text='YOU WIN! Congratulations!')
                self.player_score += 1
                player_points.configure(text=self.player_score)
            else:
                game_text.configure(text='YOU LOSE! Maybe next time!')
                self.computer_score += 1
                computer_points.configure(text=self.computer_score)


game = Game()


def create_mainframe():
    # Create app mainframe.
    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, pady=12, padx=12, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    return mainframe


def create_labels(mainframe):
    # Labels
    ttk.Label(mainframe, text='PLAYER').grid(column=1, row=1)
    ttk.Label(mainframe, text='GAME').grid(column=2, row=2)
    ttk.Label(mainframe, text='COMPUTER').grid(column=3, row=1)


def create_score(mainframe):
    global player_points, computer_points
    # Points
    points_style = ttk.Style()
    points_style .configure("style.TLabel", font=("times new roman", 30))
    player_points = ttk.Label(mainframe, text='0', style='style.TLabel')
    player_points.grid(column=1, row=2)
    computer_points = ttk.Label(mainframe, text='0', style='style.TLabel')
    computer_points.grid(column=3, row=2)


def create_game_frame(mainframe):
    global game_text
    # Game text
    game_frame = ttk.Frame(mainframe, width=400, height=100, borderwidth=2, relief=GROOVE)
    game_frame.grid(column=2, row=3, padx=5, pady=15)
    game_frame.grid_propagate(0)
    text_style = ttk.Style()
    text_style.configure("text_style.TLabel", font=("times new roman", 18))
    game_text = ttk.Label(game_frame, text='Choose your weapon and click fight.', style='text_style.TLabel',
                          anchor='center')
    game_text.place(relx=0.5, rely=0.5, anchor="center")


def create_button(mainframe):
    # Fight button
    button_style = ttk.Style()
    button_style.configure("style.TButton", font=("times new roman", 18))
    fight_button = ttk.Button(mainframe, text='FIGHT!', style='style.TButton', command=game.start)
    fight_button.grid(column=2, row=4)


def create_weapon_buttons(mainframe):
    global weapons
    # Weapon select
    weapon_frame = ttk.Frame(mainframe)
    weapon_frame.grid(column=2, row=5, pady=12)
    weapons = StringVar()
    rock = ttk.Radiobutton(weapon_frame, image=img.rock_small_photo, variable=weapons, value='rock',
                           command=img.select_weapon)
    rock.grid(column=1, row=1)
    paper = ttk.Radiobutton(weapon_frame, image=img.paper_small_photo, variable=weapons, value='paper',
                            command=img.select_weapon)
    paper.grid(column=2, row=1)
    scissors = ttk.Radiobutton(weapon_frame, image=img.scissors_small_photo, variable=weapons, value='scissors',
                               command=img.select_weapon)
    scissors.grid(column=3, row=1)


frame = create_mainframe()
create_labels(frame)
create_score(frame)
create_game_frame(frame)
img.create_players_img(frame)
create_button(frame)
create_weapon_buttons(frame)
img.select_weapon()
root.mainloop()
