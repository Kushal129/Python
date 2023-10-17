str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = str2[:2] + str1[2:] + ' ' + str1[:2] + str2[2:]
print(result)
