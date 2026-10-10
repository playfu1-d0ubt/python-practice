import random
import tkinter as tk

MAX_HISTORY = 5
history = []  # the most recent rolls, as (die1, die2) pairs

def roll_dice():
    """Roll two dice and show each one, plus the total."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice_label.config(text=f"{die1}  and  {die2}")
    total_label.config(text=f"Total: {die1 + die2}")
    double_label.config(text=f"")
    if die1 == die2:
        double_label.config(text=f"DOUBLE")
    history.append((die1, die2))
    if len(history) > MAX_HISTORY:
        history.pop(0)  # forget the oldest roll
    show_history()


def show_history():
    """Show the recent rolls, newest first."""
    lines = []
    for die1, die2 in reversed(history):
        lines.append(f"{die1} + {die2} = {die1 + die2}")
    history_label.config(text="\n".join(lines))
        
def clear_history():
    history.clear()
    show_history()

window = tk.Tk()
window.title("Dice Game")
window.geometry("300x400")

hello = tk.Label(text="Click the button to roll the dice")
hello.pack()

# command=roll_dice has no brackets: we pass the function itself, and tkinter calls it on each click
button = tk.Button(text="Roll!", command=roll_dice)
button.pack()

dice_label = tk.Label(text="", font=("Arial", 32))
dice_label.pack()

total_label = tk.Label(text="", font=("Arial", 18))
total_label.pack()

double_label = tk.Label(text="", font=("Arial", 24))
double_label.pack()

history_title = tk.Label(text="Recent rolls", font=("Arial", 12, "bold"))
history_title.pack(pady=(5, 0))

history_label = tk.Label(text="", font=("Arial", 12))
history_label.pack()

clear= tk.Button(text="Clear History", command=clear_history)
clear.pack()

tk.mainloop()