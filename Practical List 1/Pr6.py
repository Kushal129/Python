# Write a Python program to calculate simple and compound interest. ( vyaj ganatri )
# 1 amunt(bhav)
# 2 time (ketla time purtu)
# 3 rate (vyaj ketlu lagse)

#input 
amount = float(input('Enter amount: '))
time = float(input('Enter time: '))
rate = float(input('Enter rate: '))

#calculation 

# simple interest mate paisa x time x vyaj na bhagiya 100 karvana
simple_interest = (amount*time*rate)/100
# chakravruti vyaj mate paisa x 1 + vyaj / 100 kari time guni ne - 1 karvo
compound_interest = amount * ( (1+rate/100)**time - 1)



# Out put 
print("Simple interest is: ", str (simple_interest))
print("Compound interest is:",str(compound_interest))