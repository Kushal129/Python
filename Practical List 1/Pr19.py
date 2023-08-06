# Write a Python program to input three numbers and display the maximum number

def main():
    # Get user input for three numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Find the maximum number among the three
    max_num = max(num1, num2, num3)

    # Display the result
    print(f"The maximum number is: {max_num}")

# Call the main function
main()
