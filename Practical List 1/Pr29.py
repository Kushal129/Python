# Write a python program to find reverse of number. 

num = int(input("Enter a number: "))
anum = num

# Convert the number to a string and reverse it using slicing
# slicing extract a portion of a string " [] , : " | string[start:end:step]
num_str = str(num)
reversed_str = num_str[::-1]

# Convert the reversed string back to an integer
rnum = int(reversed_str)

print(f"The reverse of {anum} is {rnum}")
