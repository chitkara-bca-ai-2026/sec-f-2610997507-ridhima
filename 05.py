# Lab 05 - Engineering Calculation Tool

import math

# 1. Accept a numerical value from the user
value = float(input("Enter a numerical value: "))

# 2. Accept an exponent and calculate the power using pow()
exponent = float(input("Enter an exponent: "))
power_result = math.pow(value, exponent)

# 3. Calculate the square root of the given value using sqrt()
sqrt_result = math.sqrt(value)

# 4. Accept a decimal measurement and find ceil() and floor()
decimal_value = float(input("Enter a decimal measurement: "))
ceil_result = math.ceil(decimal_value)
floor_result = math.floor(decimal_value)

# 5. Display all the calculated results
print("\n" + "=" * 55)
print("               ENGINEERING CALCULATION TOOL")
print("=" * 55)
print(f"Enter a numerical value: {value}")
print(f"Enter an exponent: {exponent}")
print(f"Enter a decimal measurement: {decimal_value}")

print("\n--- Results ---")
print(f"Value               : {value}")
print(f"Exponent            : {exponent}")
print(f"Power (pow)         : {power_result}")
print(f"Square Root (sqrt)  : {sqrt_result:.4f}")
print(f"Decimal Value       : {decimal_value}")
print(f"Ceil Value          : {ceil_result}")
print(f"Floor Value         : {floor_result}")
print("=" * 55)