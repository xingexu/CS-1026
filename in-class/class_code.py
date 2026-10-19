"""
CS1026 Lab 2
Name: Xinge Xu
Student ID: 251549803
Username: XXU767
Date: October 6, 2026

Class Code
"""
# Don't worry about this one right now but keep
# it in your code!
import hashlib

# So we can use random functions like
# random.choice()
import random

# Let the user set the seed to used to generate
# pseudorandom values. If they input anything
# but a non-negative whole number, use the 
# default seed (None).
seed = input("Input a seed: ")
if seed.isdecimal():
    random.seed(int(seed))
else:
    random.seed(None)

class_code = ""
VALID_CHARS = "ABCEFGHJKLMNPQRTUVWXY23456789"

for character in range(6):
    class_code += random.choice(VALID_CHARS)

print(f"Class code: {class_code}")


# Class code checker
# Don't worry how this works for now, but this code will
# tell you if the class code you generated happens to be
# the class code for today's lecture.
x = hashlib.pbkdf2_hmac("sha256", class_code.encode(), b"W2qFz10tmN", 500000).hex()
if x == "6c80d62bffa2333e62d649615961588b856d0389467f68fdb1c872a23292940a":
    print(f"\n{class_code} is today's class code!!!!")
else:
    print(f"\nSorry, {class_code} is NOT today's class code, try again!")
