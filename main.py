from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Rock Paper Scissors")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Labels
ttk.Label(mainframe, text='Player').grid(column=1, row=1, sticky=(N, W, E, S))
ttk.Label(mainframe, text='Game').grid(column=2, row=1)
ttk.Label(mainframe, text='Computer').grid(column=3, row=1)

# Game text
game_frame = ttk.Frame(mainframe, padding="12 12 12 12", borderwidth=2, relief=GROOVE)
game_frame.grid(column=2, row=2)
game_text = ttk.Label(game_frame, text='For start game choose your weapon and click fight')
game_text.grid(column=0, row=0)

# Fight button
ttk.Button(mainframe, text='FIGHT!').grid(column=2, row=3)

# Weapon choose
weapon_frame = ttk.Frame(mainframe, padding="3 3 12 12")
weapon_frame.grid(column=2, row=4)
weapons = StringVar()
rock = ttk.Radiobutton(weapon_frame, text='Rock', variable=weapons, value='rock')
rock.grid(column=1, row=1)
paper = ttk.Radiobutton(weapon_frame, text='Paper', variable=weapons, value='paper')
paper.grid(column=2, row=1)
scissors = ttk.Radiobutton(weapon_frame, text='Scissors', variable=weapons, value='scissors')
scissors.grid(column=3, row=1)

root.mainloop()