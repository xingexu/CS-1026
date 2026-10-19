# Full name: [YOUR FULL NAME]
# Student number: [YOUR STUDENT NUMBER]
# UWO username: [YOUR UWO USERNAME]
# Created: October 5, 2026
# Description: Compares a user's guesses with a binary-search computer player
# trying to find the same randomly generated integer from 1 to 1000.

import random


secret = random.randint(1, 1000)
your_count = 0

print("*** Your turn ***")
while True:
    your_count += 1
    guess = int(input(f"Your guess [{your_count}]: "))
    if guess < secret:
        print("Higher")
    elif guess > secret:
        print("Lower")
    else:
        print(f"Congratulations! The correct answer was {secret}")
        break

print("\n*** My turn ***")
low = 1
high = 1000
my_count = 0

while True:
    # Integer division rounds the midpoint down, as required.
    guess = (low + high) // 2
    my_count += 1
    print(f"My guess [{my_count}]: {guess}")
    if guess < secret:
        print("Higher")
        low = guess + 1
    elif guess > secret:
        print("Lower")
        high = guess - 1
    else:
        print(f"Congratulations! The correct answer was {secret}")
        break

print("\n*** Final score ***")
print(f"Your guess count: {your_count}")
print(f"My guess count:   {my_count}")
if your_count < my_count:
    print("You win!")
elif your_count > my_count:
    print("I win!")
else:
    print("We tied!")
