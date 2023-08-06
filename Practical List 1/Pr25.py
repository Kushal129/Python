# Write a python program to check whether the number is odd or even.

def ev_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

num = int(input("Enter the number: "))
ans = ev_odd(num)
print(f"The  {num}  is  {ans}  Number")
