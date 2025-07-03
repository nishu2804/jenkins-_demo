import sys

year = 2024  # Change this to a leap year to pass

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
    sys.exit(0)  # Jenkins: SUCCESS
else:
    print(f"{year} is not a leap year")
    sys.exit(1)  # Jenkins: FAILURE

