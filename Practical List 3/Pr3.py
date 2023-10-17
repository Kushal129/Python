# 3. Write a Python program to count the number of strings in list where the string
# length is 2 or more and the first and last character are same.
# Sample List: ['abc', 'xyz', 'aba', '1221']
# Output: 2


my_list = ['abc', 'xyz', 'aba', '1221']
count = 0

# Iterate through the list and check each string
for s in my_list:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Output:", count)
