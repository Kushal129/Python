# 3. Write a Python program to count the number of strings in list where the string
# length is 2 or more and the first and last character are same.
# Sample List: ['abc', 'xyz', 'aba', '1221']
# Output: 2

my_list = ['abc', 'xyz', 'aba', '1221']
count = sum(1 for item in my_list if len(item) >= 2 and item[0] == item[-1])
print("Count:", count)
