# Write a Python program to find remainder of division operation where the
# dividend and divisor are both natural number.

def main():
    # Get user input for dividend and divisor (natural numbers)
    dividend = int(input("Enter the dividend (natural number): "))
    divisor = int(input("Enter the divisor (natural number): "))

    # Calculate the remainder using the modulo operator
    remainder = dividend % divisor

    # Display the result
    print(f"The remainder of {dividend} divided by {divisor} is {remainder}.")

# Call the main function
main()
