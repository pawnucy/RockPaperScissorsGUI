from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock Paper Scissors")


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

    def select_weapon(self, weapon):
        # Updates player image when weapon is selected
        if weapon == 'rock':
            self.player_img.configure(image=self.rock_photo)
        elif weapon == 'paper':
            self.player_img.configure(image=self.paper_photo)
        elif weapon == 'scissors':
            self.player_img.configure(image=self.scissors_photo)


img = Img()


class GameInterface:
    """ Class responsible for creating the game interface. """
    def __init__(self, root):
        self.root = root
        self.mainframe = None
        self.game_text = None
        self.player_points = None
        self.computer_points = None
        self.fight_button = None
        self.weapons = StringVar()

    def create_mainframe(self):
        """ Create the main frame of the app. """
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, pady=12, padx=12, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        return self.mainframe

    def create_labels(self):
        """ Create the labels for the game. """
        ttk.Label(self.mainframe, text='PLAYER').grid(column=1, row=1)
        ttk.Label(self.mainframe, text='GAME').grid(column=2, row=2)
        ttk.Label(self.mainframe, text='COMPUTER').grid(column=3, row=1)

    def create_score(self):
        """ Create the score labels for the game. """
        points_style = ttk.Style()
        points_style.configure("style.TLabel", font=("times new roman", 30))
        self.player_points = ttk.Label(self.mainframe, text='0', style='style.TLabel')
        self.player_points.grid(column=1, row=2)
        self.computer_points = ttk.Label(self.mainframe, text='0', style='style.TLabel')
        self.computer_points.grid(column=3, row=2)

    def create_game_frame(self):
        """ Create the game frame for the app. """
        game_frame = ttk.Frame(self.mainframe, width=400, height=100, borderwidth=2, relief=GROOVE)
        game_frame.grid(column=2, row=3, padx=5, pady=15)
        game_frame.grid_propagate(0)
        text_style = ttk.Style()
        text_style.configure("text_style.TLabel", font=("times new roman", 18))
        self.game_text = ttk.Label(game_frame, text='Choose your weapon and click fight.', style='text_style.TLabel',
                                   anchor='center')
        self.game_text.place(relx=0.5, rely=0.5, anchor="center")

    def create_weapons_buttons(self):
        # Weapon select
        weapon_frame = ttk.Frame(self.mainframe)
        weapon_frame.grid(column=2, row=5, pady=12)
        self.weapons = StringVar()
        rock = ttk.Radiobutton(weapon_frame, image=img.rock_small_photo, variable=self.weapons, value='rock',
                               command=lambda: img.select_weapon('rock'))
        rock.grid(column=1, row=1)
        paper = ttk.Radiobutton(weapon_frame, image=img.paper_small_photo, variable=self.weapons, value='paper',
                                command=lambda: img.select_weapon('paper'))
        paper.grid(column=2, row=1)
        scissors = ttk.Radiobutton(weapon_frame, image=img.scissors_small_photo, variable=self.weapons, value='scissors',
                                   command=lambda: img.select_weapon('scissors'))
        scissors.grid(column=3, row=1)

    def create_fight_button(self):
        """ Create the fight button for the app. """
        button_style = ttk.Style()
        button_style.configure("style.TButton", font=("times new roman", 18))
        self.fight_button = ttk.Button(self.mainframe, text='FIGHT!', style='style.TButton', command=self.start_game)
        self.fight_button.grid(column=2, row=4)

    def start_game(self):
        """ Start the game by pressing the fight button. """
        game.start()


interface = GameInterface(root)


class Game:
    """ Class responsible for game logic. """

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.choices = ['rock', 'paper', 'scissors']

    def start(self):
        """ Start the game by pressing the fight button. """
        computer_choice = random.choice(self.choices)
        if interface.weapons.get() == "":
            interface.game_text.configure(text='Please select your weapon!')
        else:
            img.computer_img_replace(computer_choice)
            if interface.weapons.get() == computer_choice:
                interface.game_text.configure(text='DRAW! There is no winner!')
            elif (interface.weapons.get() == 'rock' and computer_choice == 'scissors') or \
                    (interface.weapons.get() == 'paper' and computer_choice == 'rock') or \
                    (interface.weapons.get() == 'scissors' and computer_choice == 'paper'):
                interface.game_text.configure(text='YOU WIN! Congratulations!')
                self.player_score += 1
                interface.player_points.configure(text=self.player_score)
            else:
                interface.game_text.configure(text='YOU LOSE! Maybe next time!')
                self.computer_score += 1
                interface.computer_points.configure(text=self.computer_score)


game = Game()
frame = interface.create_mainframe()
interface.create_labels()
interface.create_score()
interface.create_game_frame()
img.create_players_img(frame)
interface.create_fight_button()
interface.create_weapons_buttons()
root.mainloop()
