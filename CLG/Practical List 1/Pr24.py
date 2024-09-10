# Write a Python program that takes any character as an input and check
# whether it is alphabet,digit or special character.
# num = input("wrire word : ")
# if(num.isalpha()):
#     print("Alphabet : True")
# else:
#     print("Alphabet : False")
# if(num.isdigit()):
#     print("Digit : True")
# else:
#     print("Digit : False")
# 1

def has_numbers(input_str):
    return any(char.isdigit() for char in input_str)

def has_alphabets(input_str):
    return any(char.isalpha() for char in input_str)

def has_special_characters(input_str):
    return any(not char.isalnum() for char in input_str)

# Get input string from user
input_str = input("Enter a string: ")

# Check and display whether the string contains numbers, alphabets, and special characters
print(f"Contains Numbers: {has_numbers(input_str)}")
print(f"Contains Alphabets: {has_alphabets(input_str)}")
print(f"Contains Special Characters: {has_special_characters(input_str)}")

