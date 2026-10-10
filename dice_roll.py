import random
import tkinter as tk

def roll_dice():
    """Roll two dice and show each one, plus the total."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    dice_label.config(text=f"{die1}  and  {die2}")
    total_label.config(text=f"Total: {die1 + die2}")
    double_label.config(text=f"")
    if die1 == die2:
        double_label.config(text=f"DOUBLE")
        

window = tk.Tk()
window.title("Dice Game")
window.geometry("300x300")

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

tk.mainloop()