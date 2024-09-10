# Write a Python program to find the largest and smallest among three
# entered numbers and also display whether the identified largest/smallest
# numberis evenorodd



def ev_odd(num):
    return "Even" if num % 2 == 0 else "odd"
 
# input
num1 = float (input ("Enter NUmber 1:- "))
num2 = float (input ("Enter NUmber 2:- ")) 
num3 = float (input ("Enter NUmber 3:- ")) 

# chack larg small 
lar = max(num1 , num2 , num3)
smal = min(num1 , num2 , num3)

largest= ev_odd(lar)
smallest = ev_odd(smal)

print (f"Largest Number :-  {lar } ({largest})" )
print (f"Smallest Number :-  {smal } ({smallest})" )
