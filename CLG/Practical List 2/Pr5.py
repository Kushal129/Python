# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' at the end
# of string. If the string length of the given string is less than 3, leave it unchanged
# and print string as it is.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


s = input("Enter a string: ")
if len(s) < 3:
    print(s)
elif s.endswith('ing'):
    print(s + 'ly')
else:
    print(s + 'ing')
