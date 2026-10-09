"""Secret Message Bot.

Turns a message into a list of character codes (e.g. "Hi" -> 72, 105)
and back again, using ord() and chr().
"""


def encode():
    message = input("Enter your secret message: ")
    codes = []
    for character in message:
        codes.append(ord(character))  # ord() turns a character into its number
    print("Encoded:", ", ".join(str(code) for code in codes))


def decode():
    text = input("Enter the numbers, separated by commas: ")
    message = ""
    for part in text.split(","):
        try:
            message += chr(int(part))  # chr() turns a number back into a character
        except (ValueError, OverflowError):
            print(f"'{part.strip()}' isn't a valid character code.")
            return
    print("Decoded:", message)


while True:
    print("\n1 to encode, 2 to decode, 0 to exit")
    choice = input(":").strip()
    if choice == "1":
        encode()
    elif choice == "2":
        decode()
    elif choice == "0":
        break
    else:
        print("Invalid choice, try again.")
