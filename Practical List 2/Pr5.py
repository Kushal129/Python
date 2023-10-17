s = input("Enter a string: ")
if len(s) < 3:
    print(s)
elif s.endswith('ing'):
    print(s + 'ly')
else:
    print(s + 'ing')
