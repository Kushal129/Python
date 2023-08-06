# Write a Python program to find whether the given year is a leap year or not.
# (A year is leap if it is divisible by 4 and divisible by 100 or 400.)


def main():
    # Get user input for the year
    year = int(input("Enter a year: "))

    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        # F --> conovert direct no need to  explicit conversions..
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# Call the main function
main()
