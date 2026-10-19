"""
CS1026 Week 3 Activity: Postal Code Checker
Name: Xinge Xu
Student ID: 251549803
Username: XXU767
Date: September 22, 2026

this program reads a Canadian postal code, and then adjusts it by removing
spaces, uppercase, validates the structure, and only if valid prints a
formatted postal code and a broad region.
"""

# Geting and normalize input
raw = input("Enter a Canadian postal code: ")

raw = raw.upper()
raw = raw.replace(" ", "")


# Validating the postal code

# Checking if it has exactly 6 characters
if len(raw) != 6:
    print("Invalid postal code: Bad length!")

# Checking if  characters 1, 3, and 5 are letters
elif not raw[0].isalpha() or not raw[2].isalpha() or not raw[4].isalpha():
    print("Invalid postal code: Letter check failed!")

# Check if characters 2, 4, and 6 are numbers
elif not raw[1].isdecimal() or not raw[3].isdecimal() or not raw[5].isdecimal():
    print("Invalid postal code: Number check failed!")

# only f valid, thne format as well as print the postal code
else:
    print("Validated Postal Code: " + raw[:3] + " " + raw[3:])

    # Step 4: Determine the region
    if raw[0] in "ABCE":
        print("Region: Atlantic Canada")

    elif raw[0] in "GHJ":
        print("Region: Quebec")

    elif raw[0] in "KLMNP":
        print("Region: Ontario")

    elif raw[0] in "RSTV":
        print("Region: Prairies/BC")

    elif raw[0] in "XY":
        print("Region: Territories")

    else:
        print("Error not a valid region!")