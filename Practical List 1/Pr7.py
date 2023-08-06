# Write a Python program to find average of any two numbers.
def average (num1 , num2):
    return (num1 + num2)/2
num1 = int (input("Enter Number 1 :- "))
num2 = int (input("Enter Number 2 :- "))
avg =average(num1, num2)
print ("Average is :- " ,str(avg))