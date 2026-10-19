"""
CS1026 Lab 3
Name: Xinge Xu
Student ID: 251549803
Username: XXU767
Date: October 8, 2026

This program allows the user to enter product information for an order,
including product name, quantity, and unit price. It calculates the total
cost of the order, identifies the most expensive item,
and computes the average unit price of all products entered.
The program continues to prompt for product information
until the user indicates they are done.
"""

print("MyShoppe Order Entry")
print("--------------------")

order_total = 0
most_expensive_item = ""
highest_price = -1
price_total = 0
product_count = 0

while True:
    product_name = input("Enter product name (or 'done' to finish): ")
    if product_name.strip().lower() == "done":
        break

    quantity = int(input("Enter quantity: "))
    while quantity <= 0:
        print("Quantity must be greater than 0.")
        quantity = int(input("Enter quantity: "))

    unit_price = float(input("Enter unit price: "))
    while unit_price < 0:
        print("Unit price cannot be negative.")
        unit_price = float(input("Enter unit price: "))

    item_total = quantity * unit_price
    order_total += item_total
    print(f"Item total: ${item_total:.2f}")
    print()

    if unit_price > highest_price:
        most_expensive_item = product_name
        highest_price = unit_price

    price_total += unit_price
    product_count += 1

print()
print("Order Summary")
print("-------------")
print(f"Order total: ${order_total:.2f}")
if product_count > 0:
    average_price = price_total / product_count
    print(f"Most expensive item: {most_expensive_item}")
    print(f"Unit price: ${highest_price:.2f}")
    print(f"Average unit price: ${average_price:.2f}")
else:
    print("No products entered.")