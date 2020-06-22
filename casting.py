"""
Program: cast_to_integer.py
Author: Sherri Maya
Last date modified: 06/21/2020



The purpose of this program is to accept any input,
convert to a integer type and output the integer.
"""
x = input('Enter your anything:')
try:
    x = int(float(x))
    print(x)
except ValueError:
    print(x)

# Input   Expected Output  Actual Output
#   7           7               7
#  1.2          2               2
# 20.8578965   20              20
# 'cat'        cat             cat
