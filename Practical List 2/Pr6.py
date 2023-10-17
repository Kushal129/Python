s = input("Enter a string: ")
n = int(input("Enter the index to remove: "))
result = s[:n] + s[n+1:]
print(result)
