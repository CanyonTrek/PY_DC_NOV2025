#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO COPY and optionally FILTER
# collections (str/list/tuple/dict/set)
""" 
    DocString
"""
students = ['asma', 'mike', 'ganga', 'dave', 'paulina', 'courtney', 'rodanthi', 'tanvi', 'mike']

# Iterate through the Source collection and optionally filter it to a destination collection.
# 1.Using an ITERATOR loop + source, optional condition (filtering), an expression
wee_names = []
for name in students: # 1.Iterator loop + source
    if len(name) <= 5: # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"1.Short names = {wee_names}")

def filter_names(name):
    """ Return True if name is short """
    if len(name) <= 5:
        return True
    else:
        return False

# 2.Using an ITERATOR loop + source, user function (filtering), an expression
wee_names = []
for name in students: # 1.Iterator loop + source
    if filter_names(name): # 2.Optional condition (filtering)
        wee_names.append(name.upper()) # 3.Expression
print(f"2.Short names = {wee_names}")

# 3.Using built-in filter() function (Iteration), user function (Filtering)
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4.Using built-in filter() function (Iteration), lambda function (Filtering)
wee_names = list(filter(lambda name: len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

# 5.Using LIST COMPREHENSION - expression, iterator loop + source, optional condition
wee_names = [ name.upper() for name in students if len(name) <= 5 ]
print(f"5.Short names = {wee_names}")

# 5.1 Using LIST COMPREHENSION - expression, iterator loop + source, optional condition
wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ]
print(f"5.1.Short names = {wee_names}")

# 5.2 Using DICT COMPREHENSION - expression, iterator loop + source, optional condition
# EXTRA FREE FILTERING - dict remove DUPLICATE KEYS!
wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 }
print(f"5.2.Short names = {wee_names}")

# 5.3 Using SET COMPREHENSION - expression, iterator loop + source, optional condition
# EXTRA FREE FILTERING - set remove DUPLICATE VALUES!
wee_names = { name.upper() for name in students if len(name) <= 5 }
print(f"5.3.Short names = {wee_names}")