s = input("Enter a string: ")
if len(s) < 2:
    print(s)
else:
    result = s[-1] + s[1:-1] + s[0]
    print(result)
