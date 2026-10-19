# Full name: [YOUR FULL NAME]
# Student number: [YOUR STUDENT NUMBER]
# UWO username: [YOUR UWO USERNAME]
# Created: October 5, 2026
# Description: Simulates a ten-floor elevator with restricted access and
# maintenance required after ten successful trips.


def move_elevator(floor, target):
    # Show every floor passed, including the target floor.
    print(f"Moving to floor {target}")
    while floor != target:
        if floor < target:
            floor += 1
        else:
            floor -= 1
        print(floor)
    print(f"Arrived at floor {target}")
    return floor


floor = 1
uses = 0

while True:
    command = input("Input: ")
    if command == "q":
        break
    if command == "m":
        if floor == 1:
            uses = 0
            print("MAINTENANCE COMPLETE!")
        else:
            print("MAINTENANCE CAN ONLY BE PERFORMED ON FLOOR 1!")
        continue

    # Check for an optional sign followed by digits before using int().
    digits = command.strip()
    if digits != "" and (digits[0] == "-" or digits[0] == "+"):
        digits = digits[1:]
    valid = digits != ""
    for char in digits:
        if char < "0" or char > "9":
            valid = False
            break
    if not valid:
        print("UNRECOGNIZED COMMAND!")
        continue
    target = int(command)

    if uses >= 10:
        print("OUT OF ORDER. MAINTENANCE REQUIRED!")
        continue
    if target < 1 or target > 10:
        print("INVALID FLOOR!")
        continue
    if target == floor:
        print(f"ALREADY ON FLOOR {target}!")
        continue

    if target == 3 or target == 4:
        card = input("Present key card: ")
        if ((target == 3 and card != "Red")
                or (target == 4 and card != "Blue")):
            print("ACCESS DENIED!")
            continue

    floor = move_elevator(floor, target)
    uses += 1

    # The automatic return does not count as a user trip.
    if uses == 10:
        print("OUT OF ORDER. MAINTENANCE REQUIRED!")
        if floor != 1:
            floor = move_elevator(floor, 1)
