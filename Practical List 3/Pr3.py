my_list = ['abc', 'xyz', 'aba', '1221']
count = sum(1 for item in my_list if len(item) >= 2 and item[0] == item[-1])
print("Count:", count)
