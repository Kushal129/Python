
# Write a Python program to check whether a number is Prime or not. (a whole 
# number  greater  than  1  that  cannot  be  exactly  divided  by  any  whole  number 
# other than itself and 1 (e.g. 2, 3, 5, 7, 11).

def prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        # range is a built-in function used to generate a sequence of numbers. 
        # It creates an immutable sequence of numbers within a specified range.
        if number % i == 0:
            return False

    return True

# Get user input
num = input("Enter a number greater than 1: ")
if num.isdigit(): #chack the value if entered value is character its give error 
    num = int(num)
    if num > 1 and prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
else:
    print("Invalid input. Please enter a valid integer greater than 1.")
