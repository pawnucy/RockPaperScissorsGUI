from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock Paper Scissors")


def select_weapon():
    # Updates player when weapon is selected
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
            game_text.configure(text='Draw! There is no winner!')
        elif (weapons.get() == 'rock' and computer_choice == 'scissors') or \
                (weapons.get() == 'paper' and computer_choice == 'rock') or \
                (weapons.get() == 'scissors' and computer_choice == 'paper'):
            game_text.configure(text='Congratulations! YOU WIN!')
            score = 'player'
            change_score(score)
        else:
            game_text.configure(text='You Lose! Maybe next time!')
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

player_score = 0
computer_score = 0
def change_score(score):
    # Changes the scoreboard.
    global player_score, computer_score
    if score == 'player':
        player_score += 1
        player_points.configure(text=player_score)
    elif score == 'computer':
        computer_score += 1
        computer_points.configure(text=computer_score)



# Images
question_img = Image.open("images/questionmark.png")
rock_img = Image.open("images/rock.png")
paper_img = Image.open("images/paper.png")
scissors_img = Image.open("images/scissors.png")

# Create PhotoImage objects from PIL Images
question_photo = ImageTk.PhotoImage(question_img)
rock_photo = ImageTk.PhotoImage(rock_img)
paper_photo = ImageTk.PhotoImage(paper_img)
scissors_photo = ImageTk.PhotoImage(scissors_img)

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, pady=12, padx=12, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Labels
ttk.Label(mainframe, text='PLAYER').grid(column=1, row=1)
ttk.Label(mainframe, text='GAME').grid(column=2, row=2)
ttk.Label(mainframe, text='COMPUTER').grid(column=3, row=1)

# Points
player_points = ttk.Label(mainframe, text='0')
player_points.grid(column=1, row=2)
computer_points = ttk.Label(mainframe, text='0')
computer_points.grid(column=3, row=2)

# Images below points
player_img = ttk.Label(mainframe, image=question_photo)
player_img.grid(column=1, row=3)
computer_img = ttk.Label(mainframe, image=question_photo)
computer_img.grid(column=3, row=3)


# Game text
game_frame = ttk.Frame(mainframe, borderwidth=2, relief=GROOVE)
game_frame.grid(column=2, row=3, padx=5, pady=15)
game_text = ttk.Label(game_frame, text='For start game choose your weapon and click fight.')
game_text.grid(column=0, row=0)

# Fight button
fight_button = ttk.Button(mainframe, text='FIGHT!', command=fight)
fight_button.grid(column=2, row=4)

# Resize images for weapon select
small_size = (100, 100)
rock_small = rock_img.resize(small_size)
rock_small_photo = ImageTk.PhotoImage(rock_small)
paper_small = paper_img.resize(small_size)
paper_small_photo = ImageTk.PhotoImage(paper_small)
scissors_small = scissors_img.resize(small_size)
scissors_small_photo = ImageTk.PhotoImage(scissors_small)

# Weapon select
weapon_frame = ttk.Frame(mainframe)
weapon_frame.grid(column=2, row=5, pady=12)
weapons = StringVar()
rock = ttk.Radiobutton(weapon_frame, image=rock_small_photo, variable=weapons, value='rock',
                       command=select_weapon)
rock.grid(column=1, row=1)
paper = ttk.Radiobutton(weapon_frame, image=paper_small_photo, variable=weapons, value='paper',
                        command=select_weapon)
paper.grid(column=2, row=1)
scissors = ttk.Radiobutton(weapon_frame, image=scissors_small_photo, variable=weapons, value='scissors',
                           command=select_weapon)
scissors.grid(column=3, row=1)

root.mainloop()
