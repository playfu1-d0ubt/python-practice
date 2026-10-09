"""Loop practice exercises.

Each exercise is a small function. Run the file and pick one from the menu.
"""


def get_whole_number(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please type a whole number.")


def print_win():
    """Print 'You win!' three times, then a closing message."""
    for _ in range(3):
        print("You win!")
    print("Congratulations")


def count_up_from_negative():
    """Print the numbers from -10 up to 0."""
    for number in range(-10, 1):  # the end of a range is not included, so 1 gives us 0
        print(number)


def times_table():
    """Print the 1 to 12 times table for a number the user chooses."""
    number = get_whole_number("Which times table? ")
    for i in range(1, 13):
        print(f"{i} x {number} = {i * number}")


def multiples_of_13():
    """Print every multiple of 13 between two numbers, including both ends."""
    start = get_whole_number("Start number: ")
    end = get_whole_number("End number: ")
    for number in range(start, end + 1):
        if number % 13 == 0:  # % gives the remainder, so 0 means it divides exactly
            print(number)


EXERCISES = {
    "1": ("Win message x3", print_win),
    "2": ("Count from -10 to 0", count_up_from_negative),
    "3": ("Times table", times_table),
    "4": ("Multiples of 13", multiples_of_13),
}


def main():
    while True:
        print("\nPick an exercise:")
        for key, (name, _) in EXERCISES.items():
            print(f"  {key}: {name}")
        print("  0: Exit")
        choice = input(":").strip()
        if choice == "0":
            break
        if choice in EXERCISES:
            EXERCISES[choice][1]()
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
