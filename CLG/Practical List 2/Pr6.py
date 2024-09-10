# 6 Write a Python program to remove the nth index character from a nonempty
# string.


s = input("Enter a string: ")
n = int(input("Enter the index to remove: "))
result = s[:n] + s[n+1:]
print(result)
