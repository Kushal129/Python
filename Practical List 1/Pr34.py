#  Write a python program to print sum of even numbers up to given N number. 
# Ex. N = 10 then 2 + 4 + 6 + 8 + 10 = 30




num = int(input("Enter a positive integer N: "))
even_sum = 0
evens = []

for num in range(2, num + 1, 2):
    even_sum += num
    # append method is used to add the string representation of the current number
    evens.append(str(num))
# concate to string using join
evens_str = ' + '.join(evens)

print(f"Even numbers: {evens_str} = {even_sum}")
