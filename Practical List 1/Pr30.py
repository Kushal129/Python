# Write a python program to print sum of digit in a number. 
# N = 1234 then 1 + 2 + 3 + 4 = 10.

num = int(input("Enter a number: "))
anum = num

# Convert the number to a string
num_str = str(num)

# Calculate the sum of digits using a loop
sum = 0
for digit_char in num_str:
    sum += int(digit_char)

print(f"The sum of the digits in {anum} is {sum}")
