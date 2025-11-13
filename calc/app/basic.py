#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines several Basic Calc app functions
""" 
    Basic Calc App with add, multiply and divide functions.
"""
import sys

def add(*args):
    """ Return SUM of all parameters as a float
    >>> add(4, 3, 2, 1)
    10.0
    >>> add(20, 30)
    50.0
    """
    sum = 0
    for num in args:
        sum += num
    return float(sum)

def mul(*args):
    """ Return PRODUCT of all parameters as a float
    >>> mul(4, 3)
    12.0
    """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places
    >>> div(4, 3)
    1.333
    """
    return round(x/z, 3)

def main():
    print("######### Basic Calc Examples ###########")
    print(f"4 + 3 + 2 + 1= {add(4, 3, 2, 1)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as a module
    import doctest
    doctest.testmod()
    main()
    sys.exit(0)