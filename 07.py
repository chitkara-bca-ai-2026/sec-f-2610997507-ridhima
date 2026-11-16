# Lab 07 - Calendar Verification System

print("=====================================================")
print("             CALENDAR VERIFICATION SYSTEM")
print("=====================================================")

# 1. Take input from the user
year = int(input("Enter year: "))

# 2. Validate the input: Ensure the year is a positive integer greater than 0
if year <= 0:
    print("Error: Year must be a positive integer greater than 0. Exiting.")
    exit()

# 3. Check leap year rules using if-else and 4. Determine calendar details
if (year % 400 == 0):
    status = "LEAP YEAR"
    days_in_year = "366 days"
    days_in_feb = "29 days"
    reason = "Century year divisible by 400"
elif (year % 100 == 0):
    status = "COMMON YEAR"
    days_in_year = "365 days"
    days_in_feb = "28 days"
    reason = "Century year not divisible by 400"
elif (year % 4 == 0):
    status = "LEAP YEAR"
    days_in_year = "366 days"
    days_in_feb = "29 days"
    reason = "Divisible by 4 and not a century year"
else:
    status = "COMMON YEAR"
    days_in_year = "365 days"
    days_in_feb = "28 days"
    reason = "Century year not divisible by 400" # Or general non-leap year case depending on formatting

# 5. Display the results clearly
print("\n" + "-" * 53)
print(f"Year: {year}")
print(f"Status: {status}")
print(f"Days in Year: {days_in_year}")
print(f"Days in February: {days_in_feb}")
print(f"Reason: {reason}")
print("-" * 53)