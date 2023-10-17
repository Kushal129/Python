# 3. Write a Python program to print a string from a given string where all
# occurrences of first character will changed to '@', except the first character
# itself.
# Sample String : 'restart'
# Expected Result : ‘resta@t'

s = input("Enter a string: ")
f_char = s[0]
m_str = f_char + s[1:].replace(f_char, '@')
print(m_str)
