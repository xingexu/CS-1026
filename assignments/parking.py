# Name: Xinge Xu
# Student Number: 251549803
# UWO Username: XXU767
# Date Created: September 17, 2026
""" Description: takes input for parking information (car license plate) as well
    as time of arrival/departure, cost of parking parking and then
    calculates parking duration and cost based on user input, and
    also displays license plate information.
"""


# 1.1 # takes user inputs
licence_plate = input("Enter licence plate: ")
arrival_hour = int(input("Enter arrival hour (0-23): "))
arrival_minute = int(input("Enter arrival minute (0-59): "))
departure_hour = int(input("Enter departure hour (0-23): "))
departure_minute = int(input("Enter departure minute (0-59): "))
rate_per_minute = float(input("Enter parking rate per minute: $"))

# 1.2 concatenates user input to format license plate
licence_plate = licence_plate.strip()
licence_plate = licence_plate.upper()
licence_plate = licence_plate.replace(" ", "-")

plate_length = len(licence_plate)

# 1.3 convert time to minutes and calculate total parking duration
arrival_in_minutes = arrival_hour * 60 + arrival_minute
departure_in_minutes = departure_hour * 60 + departure_minute
total_minutes = departure_in_minutes - arrival_in_minutes

hours_parked = total_minutes // 60
minutes_parked = total_minutes % 60

# 1.4 calculates parking rate cost to the cent
parking_cost = round(total_minutes * rate_per_minute, 2)

# 1.5 output to users!
print()
print("Licence Plate: " + licence_plate)
print("Plate Characters: " + str(plate_length))
print("Parking Duration: " + str(hours_parked) + " hours " + str(minutes_parked) + " minutes")
print("Parking Cost: $" + str(parking_cost))
