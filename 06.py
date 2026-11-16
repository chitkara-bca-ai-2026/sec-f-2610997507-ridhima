# Lab 06 - Shop Billing System

# 1. Accept the customer's name from the user
customer_name = input("Enter Customer Name: ")

# 2. Accept the name of the garment
garment_name = input("Enter Garment Name: ")

# 3. Accept the price of one garment
price_per_unit = float(input("Enter Price of one garment: "))

# 4. Accept the number of garments purchased
quantity = int(input("Enter Number of Garments: "))

# 5. Calculate the total cost using multiplication (price * quantity)
total_amount = price_per_unit * quantity

# 6. Display a simple bill containing all details
print("\n" + "=" * 50)
print("             CLOTHING STORE BILLING SYSTEM")
print("=" * 50)
print(f"Enter Customer Name: {customer_name}")
print(f"Enter Garment Name: {garment_name}")
print(f"Enter Price of one garment: {price_per_unit}")
print(f"Enter Number of Garments: {quantity}")

print("\n" + "=" * 50)
print("                           BILL")
print("=" * 50)
print(f"Customer Name      : {customer_name}")
print(f"Garment Name       : {garment_name}")
print(f"Price per Unit     : Rs. {price_per_unit}")
print(f"Quantity           : {quantity}")
print(f"Total Amount       : Rs. {total_amount}")
print("=" * 50)