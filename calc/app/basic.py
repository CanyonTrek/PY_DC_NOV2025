#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines several Basic Calc app functions
""" 
    Basic Calc App with add, multiply and divide functions.
"""
import sys

def add(*args):
    """ Return SUM of all parameters as a float """
    sum = 0
    for num in args:
        sum += num
    return float(sum)

def mul(*args):
    """ Return PRODUCT of all parameters as a float """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places """
    return round(x/z, 3)

print("######### Basic Calc Examples ###########")
print(f"4 + 3 + 2 + 1= {add(4, 3, 2, 1)}")
print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
print(f"4 / 3 = {div(4, 3)}")

sys.exit(0)