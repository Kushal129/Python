# Write a Python program to check whether the number is odd or even. 

def main():
    # Get user input for the number
    number = int(input("Enter a number: "))

    # Check if the number is odd or even
    if number % 2 == 0:
        print("The number ",str(number)," is Even.")
    else:
        print(f"The number {number} is Odd.")

# Call the main function
main()
