"""
CS1026 Lab 1
Name: Xinge Xu
Student ID: 251549803
Username: XXU767
Date: September 24, 2026

the program I made creates a simple inventory systemfor MyShoppe. first it asks an employee
for the shop name, number of rings, glasses, and hats, as well as the price ofcd
one ring. then, it calculates the total number of items and the value of the
ring inventory, which then decides if the inventory is low, meaning less than 10 items.
finally, it  prints a formatted inventory report.
"""

# user input 
shopName = input("Enter the shop name: ")
ringQTY = int(input("Enter the number of rings: "))
ringPrice = float(input("Enter the price of one ring: ")) # since price may have decimals
glassesQTY = int(input("Enter the number of glasses: "))
hatQTY = int(input("Enter the number of hats: "))

# calculations for total number of items in stock as well as total value of the rings
total = ringQTY + glassesQTY + hatQTY
ringValue = ringQTY * ringPrice
lowInventory = total < 10 # if total is less than 10, then it's low inventory


# output for the finalized report 
print("\n\"MyShoppe Inventory Report\"")
print(f"Shop: {shopName}")
print(f"Rings: {ringQTY}")
print(f"Ring price: ${ringPrice:.2f}")
print(f"Ring inventory value: ${ringValue:.2f}")
print(f"Glasses: {glassesQTY}")
print(f"Hats: {hatQTY}")
print(f"Total items: {total}")
print(f"Low inventory: {lowInventory}")