# Sum of number digits in List
# -------------------------\n
# Method #1 : Using loop + str()
# -----------------------------\n
test_list = [12, 67, 98, 34]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Sum of number digits in List
# using loop + str()
res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
     
# printing result 
print ("List Integer Summation : " + str(res))
print(' ')
'''
# Method #2 : Using sum() + list comprehension
# -------------------------------------------\n
# Python3 code to demonstrate 
# Sum of number digits in List
# using sum() + list comprehension
 
# Initializing list
test_list = [12, 67, 98, 34]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Sum of number digits in List
# using sum() + list comprehension
res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))
     
# printing result 
print ("List Integer Summation : " + str(res))
print(' ')
'''
# Method #3 : Using sum() + reduce()
# --------------------------------\n
# Python3 code to demonstrate
# Sum of number digits in a List
# using sum() + reduce()
from functools import reduce
 
# Initializing list
test_list = [12, 67, 98, 34]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Sum of number digits in List
# using sum() + reduce()
res = [reduce(lambda x, y: int(x) + int(y), list(str(i))) for i in test_list]
 
# printing result
print("List Integer Summation : " + str(res))
print(' ')
# Method #4 : Using numpy
# -----------------------\n
import numpy as np
 
# Initializing list
test_list = [12, 67, 98, 34]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Sum of number digits in List
# using numpy
res = np.sum([list(map(int, str(ele))) for ele in test_list], axis=1)
 
# printing result
print("List Integer Summation : " + str(list(res)))
print(' ')
# Method #5 : Using itertools library:
# -------------------------------------\n
# Python3 code to demonstrate 
# Sum of number digits in List
# using itertools library
# importing itertools library
import itertools
# Initializing list
test_list = [12, 67, 98, 34]
# printing original list
print("The original list is : " + str(test_list))
# Sum of number digits in List
# using itertools library
res = [sum(map(int, list(itertools.chain(*str(ele))))) for ele in test_list]
# printing result 
print ("List Integer Summation : " + str(res))
#This code is contributed by Jyothi pinjala.
print(' ')
# Method #6 : Using map() function and modulo operator :
# -----------------------------------------------\n
lst = [12, 67, 98, 34]
def digit_sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum
 
def sum_of_digits_list(lst):
    return list(map(digit_sum, lst))
 
print(sum_of_digits_list(lst))
print(' ')
# Method #7: Creating a expression without changing to a string
# ---------------------------------------------------------\n
# Initializing list
test_list = [12, 67, 98, 34]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Sum of number digits in List
# creating an expression
res = list(sum(int(digit) for digit in str(num)) for num in test_list)
# printing result
print("List Integer Summation : " + str(list(res)))
print(' ')
# --------------------------------------------------------\n












































































































