s = input("Enter a string: ")
first_char = s[0]
modified_str = first_char + s[1:].replace(first_char, '@')
print(modified_str)
