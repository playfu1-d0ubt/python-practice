import random
import tkinter as tk

def roll_dice():
    """Pick a number from 1 to 6 and show it."""
    result = random.randint(1, 6)
    result_label.config(text=f"You rolled a {result}")

window = tk.Tk()
window.title("Dice Game")
window.geometry("300x300")

# command=roll_dice has no brackets: we pass the function itself, and tkinter calls it on each click
button = tk.Button(text="Roll!", command=roll_dice)
button.pack()

result_label = tk.Label(text="", font=("Arial", 32))
result_label.pack()

tk.mainloop()