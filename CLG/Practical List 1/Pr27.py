#  Write  a  python  program  to  find  the  sum  of  the  first  N  natural  numbers.  
# [Hint:1+2+3+4+....+N]

N = int(input("Enter a positive Number: "))
sn = 0

for num in range(1, N + 1):
    sn += num

print(f"The sum of the {N} number is : {sn}")
