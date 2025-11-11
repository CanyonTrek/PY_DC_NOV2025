#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO ITERATE through sequences
# using an ITERATOR for loop.
""" 
    DocString
"""
import sys

#                 0               1            2           3           4           5
persons = ['edward cullen', 'charlie chaplin', 'greta', 'allan carr', 'ronaldo', 'Einstein']

# ITERATE through a sequence (str/tuple/list/set/dict) one object at a time
# USING an ITERATOR for loop.
for name in persons:
    print(name, end="\n")
print("People =", persons)

# ITERATE through LIST and MODIFY values inside
idx = 0
for name in persons:
    print(name.upper(), end="\n")
    persons[idx] = name.upper()
    idx += 1
print("Persons =", persons)

# ITERATE through LIST and MODIFY values using an ITERATOR loop plus enumerate() function
for (idx, name) in enumerate(persons):
    print(name.title(), end="\n")
    persons[idx] = name.title()
print("Persons =", persons)

try:
    sys.exit(10) # Explicit EXIT with return code (0=success, 1-255=error)
except SystemExit:
    print("Quitting program..")
    sys.exit(0)