# Write a Python program to convert Kilogram into Gram

def main():
    # Get user input for kilograms
    kilograms = float(input("Enter the weight in Kilograms: "))

    # Convert Kilograms to Grams
    grams = kilograms * 1000

    # Display the result
    print(str(kilograms) + " Kilograms is equal to " + str(grams) + " Grams.")

# Call the main function
main()
