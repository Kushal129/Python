# Write a python program to print sum of odd numbers up to given N number. 
# Ex. N = 10 then 1 + 3 + 5 + 7 + 9 = 25.


num = int(input("Enter Number : "))
odd_sum = 0
odd = []

for num in range(1, num + 1, 2):
    odd_sum += num
    # append method is used to add the string representation of the current number
    odd.append(str(num))
# concate to string using join
odd_str = ' + '.join(odd)

print(f"Odd numbers: {odd_str} = {odd_sum}")

