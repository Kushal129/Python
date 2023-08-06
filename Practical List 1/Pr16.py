# Write a Python program to check whether the number is positive, negative or zero

def main():
    # Get user input for the number
    num = float(input("Enter a number: "))

    # Check if the number is positive, negative, or zero
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# Call the main function
main()
