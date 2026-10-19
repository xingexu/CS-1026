"""
CS1026 Week 4 Activity: Hangman
Name: Xinge Xu
Student ID: 251549803
Username: XXU767
Date: September 29, 2026

This program is a Hangman game where a user guesses
one letter at a time to reveal a secret word. The program takes input,
and then reveals all occurrences of correctly guessed letters,
and allows the user to make six incorrect guesses. If the user guesses
the word within these guesses, the user wins, otherwise the user loses. 
A final message is outputted to indicate whether the user has won or lost the game.
"""

SECRET = "SUCCESS" # word on the projector
MAX_WRONG = 6
blanks = "_" * len(SECRET)
wrong = 0

while wrong < MAX_WRONG:
    left = MAX_WRONG - wrong
    print(f"\nAttempts Left: {left}")
    print(f"Guessed letters: {blanks}\n")

    letter = input("Input your guess: ").upper()
    while len(letter) != 1 or not letter.isalpha():
        print("Invalid input, try again!")
        letter = input("Input your guess: ").upper()

    if letter in SECRET.upper():
        print("Letter correct!")
        new_blanks = ""
        for i in range(len(SECRET)):
            if letter == SECRET[i].upper():
                new_blanks += letter
            else:
                new_blanks += blanks[i]
        blanks = new_blanks
    else:
        print("Letter incorrect!")
        wrong += 1

    if "_" not in blanks:
        break

if wrong == MAX_WRONG:
    print("\nGAME OVER!")
else:
    print("\nYOU WIN!")


##################################################################
# WEEK 4 CLASS CODE GENERATOR                                    #
# Copy and paste this to the bottom of your hangman.py file.     #
# Don't make any changes to this code, and only update the       #
# value of SECRET at the top of hangman.py to what you see       #
# is given on the projector.                                     #
#                                                                #
# Make sure your blanks and wrong variables are named correctly  #
# and you have updated the value of SECRET.                      #
#                                                                #
# Don't worry how this code works, it is just to get the         #
# class code.                                                    #
##################################################################
if 'blanks' not in vars() or 'wrong' not in vars() or 'SECRET' not in vars():
    print("\nOne of the variables 'blanks', 'wrong', or 'SECRET' is named wrong or missing.")
    print("This code must be pasted at the end of hangman.py and your variables named correctly.")
    exit()
elif wrong != 0:
    print("\nYou must play the game and make no errors to get the class code!")
    exit()
import hashlib
data = hashlib.sha256(f"{SECRET.strip().upper()}|{blanks.strip().upper()}|{wrong}|CS1026-F24".encode()).digest()
letters, digits = "ACDEHJKMNPQRTUVWXY", "3479"
code = letters[data[0] % len(letters)] + letters[data[1] % len(letters)] + digits[data[2] % len(digits)]
code += letters[data[3] % len(letters)] + digits[data[4] % len(digits)] + digits[data[5] % len(digits)]
x = hashlib.pbkdf2_hmac("sha256", code.encode(), b"f8vTevgOhI", 500000).hex()
if x == "934b470778e811105180ad6bbed6da328df16200ef902cff0c0df47d772c6f80":
    print(f"\n{code} is the correct class code for today!")
else:
    print("\nERROR: Your result is incorrect. Check your program and ensure you gave the correct inputs.")
