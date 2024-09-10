# Write a python program to find N! (5 factorial=1*2*3*4*5 )

num = int(input("Enter a Number:-  "))

if num < 0:
    print("Enter Positive Number ")
else:
    fec = 1
    for num in range(1, num + 1):
        fec *= num

    print(f"[ {num}! = {fec} ]")
