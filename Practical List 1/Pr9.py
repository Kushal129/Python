# Write a Python program to display the size of every data type.
import sys
# The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. 
# It lets us access system-specific parameters and functions.
print("Size of int:", sys.getsizeof(int()))
print("Size of float:", sys.getsizeof(float()))
print("Size of bool:", sys.getsizeof(bool()))
print("Size of str:", sys.getsizeof(str()))
print("Size of list:", sys.getsizeof(list()))
print("Size of tuple:", sys.getsizeof(tuple()))
print("Size of dict:", sys.getsizeof(dict()))
print("Size of complex:", sys.getsizeof(complex()))
