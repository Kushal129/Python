# 2. Write a Python program to print a string made of the first two and the last two
# characters from a given a string. If the string length is less than 2, then print
# “Empty String”
# Sample String : 'Python'
# Expected Result : 'Pyon'
# Sample String : 'PY'
# Expected Result : 'PYPY'
# Sample String : ' P'
# Expected Result : “Empty String”


s = input("Enter a string: ")
if len(s) < 2:
    print("Empty String")
else:
    result = s[:2] + s[-2:]
    print(result)
