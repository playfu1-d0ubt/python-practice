# Python Practice

Small Python programs that practise the fundamentals: loops, lists, functions, user input and character codes. Each one is short enough to read in a few minutes.

## What's in here

| File | What it does | Practises |
| --- | --- | --- |
| `message_bot.py` | Turns a message into a list of numbers and back again | `ord()`, `chr()`, loops, lists, functions, input checking |
| `exercises/loops.py` | A menu of four loop exercises (counting, times tables, multiples of 13) | `for` loops, `range()`, `%`, input checking |
| `exercises/ascii_names.py` | Shows the ASCII code of every character in two names | `ord()`, list comprehensions |

## How to run

You need Python 3. There's nothing to install.

```bash
git clone git@github.com:YOUR-USERNAME/python-practice.git
cd python-practice
python3 message_bot.py
python3 exercises/loops.py
python3 exercises/ascii_names.py
```

## Example

`message_bot.py` encodes text into character codes, and decodes the same numbers back into text:

```
1 to encode, 2 to decode, 0 to exit
:1
Enter your secret message: Hi
Encoded: 72, 105

1 to encode, 2 to decode, 0 to exit
:2
Enter the numbers, separated by commas: 72, 105
Decoded: Hi
```

Every program checks its input, so typing letters where a number is expected gives a message and asks again instead of crashing.

## Notes

- These started as early practice exercises that I later tidied up: clearer names, comments, input checking and small bug fixes.
- ASCII codes only cover basic characters, but `ord()` works with any character, so accented letters like `é` are handled too.
