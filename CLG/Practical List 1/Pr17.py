# Write a Python program to check whether the number is divisible by 5 or not.
def main():
    # Get user input for the number
    num = int(input("Enter a number: "))

    # Check if the number is divisible by 5
    if num % 5 == 0:
        print("The number is divisible by 5.")
    else:
        print("The number is not divisible by 5.")

# Call the main function
main()
