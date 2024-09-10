# 8. Write a Python program to remove the characters which have odd index values
# of a given string.
# Write a Python program that takes string from the user and displays that string
# in upper and lower cases.


s = input("Enter a string: ")
result = s[::2]  # Removes characters with odd indices
print(f"Original String: {s}")
print(f"Uppercase: {result.upper()}")
print(f"Lowercase: {result.lower()}")
