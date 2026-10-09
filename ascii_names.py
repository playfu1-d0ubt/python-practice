"""Show the ASCII code of every character in two names."""

first = input("Enter your first name: ")
second = input("Enter your second name: ")

# ord() gives the number for a character; this builds a list of them
first_codes = [ord(character) for character in first]
second_codes = [ord(character) for character in second]

print(f"{first}: {first_codes}")
print(f"{second}: {second_codes}")
