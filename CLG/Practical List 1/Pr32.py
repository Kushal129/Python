# Python  Patterns

# P - 1 

# n = int (input("Enter Number :- "))
# for i in range(n): # 0 to n ROW |
#     for j in range(n-i-1): # Column -
#         print(" ",end="") # end bez ek line ma j jose _ _* space mate
#     for j in range(i+1): # How many star whant row is 0 i what 1 star....
#         print("*",end=" ") 
#     print ()
    
# out put :-  
"""
    *
   * *
  * * *
 * * * *
* * * * * 

""" 
# ------------------------------------------------------------------------

# P - 2

# n = int (input("Enter Number :- "))
#     # 0 to n ROW |
# for i in range(n): 
#         # Column -
#     for j in range(i):
#         print(" ",end="") # end bez ek line ma j jose _ _* space mate
#     for j in range(n-i): # How many star whant row is 0 i what 5 star , 1 so 4
#         print("*",end=" ") 
#     print()
    
# out put :-
"""
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
"""
# ------------------------------------------------------------------------

# # P - 3 
# str1 = input("Enter String: ")
# length = len(str1)

# # Reverse 
# for i in range(length - 1, -1, -1):
#     if i % 2 == 0:
#         for j in range(i + 1):
#             print(str1[j], end=" ")
#     else:
#         for j in range(i, -1, -1):
#             print(str1[j], end=" ")
#     print()


# out put :- 

"""
12345
1234
123
12
1
"""

# ------------------------------------------------------------------------

# P - 4

# n = int(input("Enter Number: "))

# # Upper 
# for i in range(n , 0 , -1): # row Dicri..form ma n to.. n =554321
#     for j in range(i,0,-1): # Left-Top 
#         print("*", end=" ")
#     for j in range( 2 * (n - i)): # middle ma space kare 
#         print(" ", end=" ")
#     for j in range(i,0,-1): # Right Top
#         print("*", end=" ")
#     print()

# # Lower 
# for i in range(1,n): # row  asenig...
#     for j in range(i + 1): # left down 
#         print("*", end=" ")
#     for j in range(2 * (n-i-1) ): # middle ma space 
#         print(" ", end=" ")
#     for j in range(i + 1): # right down 
#         print("*", end=" ")
#     print()

# out put :-

"""

* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
    
"""


# ----------------------------------------------------------------


# P - 5 

# n = int (input("Enter Number: "))
# for i in range(n - 1 ):
#     for j in range(i , n ):
#         print(" " , end="")
#     for j in range(i):
#         print("*", end="")
#     for j in range(i+1):
#         print("*" , end="")
#     print()
    
# for i in range(n):
#     for j in range(i+1):
#         print(" " , end="")
#     for j in range(i,n-1):
#         print("*", end="")
#     for j in range(i,n):
#         print("*" , end="")
#     print()
    
# out put :- 

"""  
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
"""

# ------------------------------------------------------------------------

# P - 6 

# n = int (input("Enter Number: "))
# count = 1 
# for i in range(n , 0 , -1):
#     for j in range(1,i+1):
#         print(count%2 , end=" ")
#     print()
#     if (i%2 == 0):
#         count=1
#     else:
#         count=0
        
# out put :-
"""

1 1 1 1 1 
0 0 0 0 
1 1 1 
0 0 
1 

"""

#----------------------------------------------------------------

# P - 7 
         
        #  BAKII

#----------------------------------------------------------------

# P - 8 

# n = int (input("Enter Number: "))
# for i in range(n):
#     for j in range(i + 1):
#         print(n-j, end="")
#     print()
    

# out put :-
"""

5
54
543
5432
54321

"""

#----------------------------------------------------------------

# P - 9

# n = int (input("Enter Number: "))
# for i in range(1,n+1):
#     for j in range(1 , i+1):
#         print(j%2, end=" ")
#     print()

# out put :- 

"""

1 
1 0 
1 0 1 
1 0 1 0 
1 0 1 0 1 
    
"""

#----------------------------------------------------------------

# P - 10

rows = 5
cols = 5

for i in range(rows,0,1):
    for j in range(cols,0,-1):
        if j == cols:
            print(str(i),end="")
        else:
            print('5',end="")
    print()

"""
    BAkIIII
    
"""


#----------------------------------------------------------------

# P - 11

# str1 =input("Enter String: ")
# # we can find length of the input string
# length = len (str1)
# for i in range(length): # row
#     for j in range(i+1): # column
#         print(str1[j], end=" ")
#     print()

# out put :- 

"""

A 
A B
A B C
A B C D
A B C D E

"""

#----------------------------------------------------------------

# P - 12

# str1 =input("Enter String: ")
# length = len(str1)
# for i in range(-1,length,): # row
#     for j in range(length - i): # column
#         print(str1[i], end=" ")
#     print()


