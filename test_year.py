import sys

# Hardcoded input
year = 2023  # Change this to 2024 to simulate success

# Leap year check logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year ✅")
    sys.exit(0)  # Success for Jenkins
else:
    print(f"{year} is not a leap year ❌")
    sys.exit(1)  # Failure for Jenkins
