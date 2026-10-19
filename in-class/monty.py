"""
CS1026 Lab 2
Name: Xinge Xu
Student ID: 251549803
Username: XXU767
Date: October 6, 2026

Monty Hall Game
"""


import random

print("###################################")
print("# WELCOME TO LET'S MAKE A DEAL!!! #")
print("###################################")
print("\nI'm your host, and I've got THREE doors for you today!")
print("Behind ONE door is a brand new car!!")
print("Behind the other TWO doors... goats.\n")

prize_door = random.randint(1, 3)

print("Alright, contestant, here we go!\n"
      "In front of you are three doors: Door 1, Door 2, and Door 3.\n")
player_choice = int(input("Which door do you choose? Type 1, 2, or 3: "))

if player_choice != prize_door:
    reveal_door = 6 - player_choice - prize_door
else:
    door_pick = random.randint(1, 2)
    reveal_door = ((player_choice + door_pick - 1) % 3) + 1

remaining_door = 6 - player_choice - reveal_door
print("\nAlright... I'm going to open one of the other doors....")
print(f"I'm opening Door {reveal_door}... and it's a GOAT!")
print("\nNow here's the big decision!")
print("Do you want to STAY with your original door, or SWITCH to "
      "the other unopened door?")
switch_or_stay = input("Type STAY or SWITCH: ").upper()

if switch_or_stay == "STAY":
    final_pick = player_choice
else:
    final_pick = remaining_door

print("\nAlright, final answer locked in!")
print(f"Let's reveal what's behind Door {final_pick}...\n")
if final_pick == prize_door:
    print("It's a.. CAR! YOU WIN!!!")
else:
    print("It's a.. GOAT! YOU LOSE.")
