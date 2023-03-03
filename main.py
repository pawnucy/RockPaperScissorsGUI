from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("Rock Paper Scissors")

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

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
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
game_frame = ttk.Frame(mainframe, padding="12 12 12 12", borderwidth=2, relief=GROOVE)
game_frame.grid(column=2, row=3)
game_text = ttk.Label(game_frame, text='For start game choose your weapon and click fight')
game_text.grid(column=0, row=0)

# Fight button
ttk.Button(mainframe, text='FIGHT!').grid(column=2, row=4)

# Weapon choose
weapon_frame = ttk.Frame(mainframe, padding="3 3 12 12")
weapon_frame.grid(column=2, row=5)
weapons = StringVar()
rock = ttk.Radiobutton(weapon_frame, image=rock_photo, variable=weapons, value='rock')
rock.grid(column=1, row=1)
paper = ttk.Radiobutton(weapon_frame, image=paper_photo, variable=weapons, value='paper')
paper.grid(column=2, row=1)
scissors = ttk.Radiobutton(weapon_frame, image=scissors_photo, variable=weapons, value='scissors')
scissors.grid(column=3, row=1)

root.mainloop()