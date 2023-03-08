from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock Paper Scissors")

# Variables
player_score = 0
computer_score = 0
global computer_points, player_points, player_img, computer_img, game_text, weapons


def create_mainframe():
    # Create app mainframe.
    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, pady=12, padx=12, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    return mainframe


def create_images():
    # Load images.
    question_img = Image.open("images/questionmark.png")
    rock_img = Image.open("images/rock.png")
    paper_img = Image.open("images/paper.png")
    scissors_img = Image.open("images/scissors.png")
    # Create PhotoImage objects from PIL Images
    question_photo = ImageTk.PhotoImage(question_img)
    rock_photo = ImageTk.PhotoImage(rock_img)
    paper_photo = ImageTk.PhotoImage(paper_img)
    scissors_photo = ImageTk.PhotoImage(scissors_img)
    return question_photo, rock_photo, paper_photo, scissors_photo, rock_img, paper_img, scissors_img


question_photo, rock_photo, paper_photo, scissors_photo, rock, paper, scissors = create_images()

def resize_image(rock_image, paper_image, scissors_image):
    # Resize images for weapon select
    small_size = (100, 100)
    rock_small = rock_image.resize(small_size)
    rock_small_photo = ImageTk.PhotoImage(rock_small)
    paper_small = paper_image.resize(small_size)
    paper_small_photo = ImageTk.PhotoImage(paper_small)
    scissors_small = scissors_image.resize(small_size)
    scissors_small_photo = ImageTk.PhotoImage(scissors_small)
    return rock_small_photo, paper_small_photo, scissors_small_photo


rock_photo_small, paper_photo_small, scissors_photo_small = resize_image(rock, paper, scissors)


def select_weapon():
    # Updates player image when weapon is selected
    if weapons.get() == 'rock':
        player_img.configure(image=rock_photo)
    elif weapons.get() == 'paper':
        player_img.configure(image=paper_photo)
    elif weapons.get() == 'scissors':
        player_img.configure(image=scissors_photo)


def fight():
    # Start the game by pressing the fight button.
    choices = ['rock', 'paper', 'scissors']
    # A random choice for the computer player.
    computer_choice = random.choice(choices)
    if weapons.get() == "":
        game_text.configure(text='Please select your weapon!')
    else:
        computer_img_replace(computer_choice)
        if weapons.get() == computer_choice:
            game_text.configure(text='DRAW! There is no winner!')
        elif (weapons.get() == 'rock' and computer_choice == 'scissors') or \
                (weapons.get() == 'paper' and computer_choice == 'rock') or \
                (weapons.get() == 'scissors' and computer_choice == 'paper'):
            game_text.configure(text='YOU WIN! Congratulations!')
            score = 'player'
            change_score(score)
        else:
            game_text.configure(text='YOU LOSE! Maybe next time!')
            score = 'computer'
            change_score(score)


def computer_img_replace(image):
    # Changes the image of the computer's weapons.
    if image == 'rock':
        computer_img.configure(image=rock_photo)
    elif image == 'paper':
        computer_img.configure(image=paper_photo)
    elif image == 'scissors':
        computer_img.configure(image=scissors_photo)


def change_score(score):
    # Changes the scoreboard.
    global player_score, computer_score
    if score == 'player':
        player_score += 1
        player_points.configure(text=player_score)
    elif score == 'computer':
        computer_score += 1
        computer_points.configure(text=computer_score)


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


def create_players_img(mainframe):
    global player_img, computer_img
    # Images below points.
    player_img = ttk.Label(mainframe, image=question_photo)
    player_img.grid(column=1, row=3)
    computer_img = ttk.Label(mainframe, image=question_photo)
    computer_img.grid(column=3, row=3)


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
    fight_button = ttk.Button(mainframe, text='FIGHT!', style='style.TButton', command=fight)
    fight_button.grid(column=2, row=4)


def resize_image(rock_image, paper_image, scissors_image):
    # Resize images for weapon select
    small_size = (100, 100)
    rock_small = rock_image.resize(small_size)
    rock_small_photo = ImageTk.PhotoImage(rock_small)
    paper_small = paper_image.resize(small_size)
    paper_small_photo = ImageTk.PhotoImage(paper_small)
    scissors_small = scissors_image.resize(small_size)
    scissors_small_photo = ImageTk.PhotoImage(scissors_small)

    return rock_small_photo, paper_small_photo, scissors_small_photo


def create_weapon_buttons(mainframe):
    global weapons
    # Weapon select
    weapon_frame = ttk.Frame(mainframe)
    weapon_frame.grid(column=2, row=5, pady=12)
    weapons = StringVar()
    rock = ttk.Radiobutton(weapon_frame, image=rock_photo_small, variable=weapons, value='rock',
                           command=select_weapon)
    rock.grid(column=1, row=1)
    paper = ttk.Radiobutton(weapon_frame, image=paper_photo_small, variable=weapons, value='paper',
                            command=select_weapon)
    paper.grid(column=2, row=1)
    scissors = ttk.Radiobutton(weapon_frame, image=scissors_photo_small, variable=weapons, value='scissors',
                               command=select_weapon)
    scissors.grid(column=3, row=1)


frame = create_mainframe()
create_labels(frame)
create_score(frame)
create_players_img(frame)
create_game_frame(frame)
create_button(frame)
create_weapon_buttons(frame)
select_weapon()
root.mainloop()
