# Lab 11 - Online Account Registration

# 1. Take input from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# 2. Validate the password against these rules
# - Minimum 8 characters
has_length = len(password) >= 8

# - At least one digit (0-9)
has_digit = any(char.isdigit() for char in password)

# - At least one uppercase letter (A-Z)
has_upper = any(char.isupper() for char in password)

# 3. Display the validation results
print("\n" + "=" * 55)
print("              PASSWORD VALIDATION REPORT")
print("=" * 55)
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

print("\n--- Validation Rules ---")

# Rule 1: Length check
if has_length:
    print("[PASS] Minimum 8 characters (10 characters)") # Or general length message
else:
    print("[FAIL] Minimum 8 characters")

# Rule 2: Digit check
if has_digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

# Rule 3: Uppercase check
if has_upper:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

# Final verdict check
print("\n--- Result ---")
if has_length and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("=" * 55)