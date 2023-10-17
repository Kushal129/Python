
# 7. Write a Python program to change a given 
# string to a new string where the first
# characters have been exchanged.
# Sample String : 'abcd'
# Expected Result : 'dbca'
# Sample String : ‘12345’
# Expected Result : ' 52341'.

s = input("Enter a string: ")
if len(s) < 2:
    print(s)
else:
    result = s[-1] + s[1:-1] + s[0]
    print(result)
