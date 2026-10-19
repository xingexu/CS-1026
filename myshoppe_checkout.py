"""
CS1026 Lab 2
Name: Xinge Xu
Student ID: 251549803
Username: XXU767
Date: September 29, 2026

This program asks for the user to input a customer’s name, product category, payment method,
coupon code, and order total. Then, it checks if the category and payment
method are accepted. In the case that both options are accepted, then the program validates
the coupon without regard to capitalization. The program then determines the delivery option
based on the order total, and finally outputs a thank you message.
"""

#user input for all the required information
customer_name = input("Enter your name: ")
category = input("Enter the product category: ")
payment_method = input("Enter your payment method: ")
coupon_code = input("Enter your coupon code: ")
order_total = float(input("Enter your order total: "))

print("Welcome to MyShoppe, " + customer_name + "!")

available_categories = "electronics books clothing home"

# checking the product category
if category.lower() not in available_categories:
    print("Category not available.")
else:
    # determining the payment method
    if payment_method == "Visa" or payment_method == "Mastercard":
        print("Payment method accepted.")

        # checking the coupon code
        if coupon_code.lower() == "save10":
            print("Coupon accepted!")
        else:
            print("No valid coupon was entered.")

        # determinng the delivery option and pricing
        if order_total >= 100:
            print("Express delivery is free.")
        elif order_total >= 50:
            print("Standard delivery is free.")
        else:
            print("A delivery fee applies.")

        # thank you message
        print("Thank you, " + customer_name + ", for shopping at MyShoppe!")
    else:
        print("Payment method not accepted.")
