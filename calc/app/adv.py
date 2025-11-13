#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines several advanced calc functions
""" 
    Advanced Calc Module with power, modulus and sqrt functions
"""
import sys

def power(x, z):
    """ Return Exponent of x to power z """
    return float(x**z)

def mod(x, z):
    """ Return Remainder after integer division of x by z """
    return float(x % z)

def sqrt(x):
    """ Return Square root of x """
    return float(x**0.5)

def main():
    print("----------- Advanced Calc Examples ----------")
    print(f"9**8 = {power(9, 8)}")
    print(f"90 % 80 = {mod(90, 80)}")
    print(f"\N{square root}90 = {sqrt(90)}")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as a module
    main()
    sys.exit(0)