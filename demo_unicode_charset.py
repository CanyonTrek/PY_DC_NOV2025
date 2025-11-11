#! /usr/bin/env python3
# Author: DCameron
# Description: This script will display the entire Unicode charset
""" 
    DocString
"""

# ITERATE through all of the chars in the Unicode table
# using an ITERATOR for loop plus range() function
for pos in range(0, 65536):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:
            print("")
    except UnicodeEncodeError:
        print(" ")