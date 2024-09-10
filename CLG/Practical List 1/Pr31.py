# To find total number of odd digit, even digit, sum of odd digit and sum of even 
# digit from the given number.

# ( input number ne chuta padvana ODD & EVEN ma and then eki no sum aalgthi ne beki no sum aalgthi)

n = int(input("Enter Number : "));
odd = 0
even = 0
x = 0
odd_count = 0
even_count = 0

while n > 0: #n greater 0 loop runig 
    x = n % 10 #n remainder (1234 to r= 4 so that x = 4)
    if x % 2 == 0:
        even = even + x
        even_count +=1 
    else:
        odd += x
        odd_count += 1
    n = n//10 # 1234 chaltu rese ne x ma 4 jrese so that intiger divition kari // thi , so 123 quotient are remaing...
    
print ('Even sum :- ', even  ,'|','Odd sum:- ',odd )
print ('Total Even number :- ',even_count  ,'|','Total Odd number :- ' , odd_count  )

