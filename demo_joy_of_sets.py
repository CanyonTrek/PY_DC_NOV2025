#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, and grow, and shrink
# sets (Unordered Mutable Collections with Unique values), No Duplicates
""" 
    DocString
"""

marvel_fans = {'tanvi', 'jen', 'sabi', 'dave', 'ganga', 'asma', 'donald'}
dc_fans = set() # Create an Empty SET

# Grow a set..
dc_fans.add("donald")
dc_fans.add("paulina")
dc_fans.add("rodanthi")

# Shrink a set..
# dc_fans.pop() # Randomly remove a value

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")
print("-" * 60)

# Combine SETS using SET operators using METHODS (Remember VENN diagrams).
print(f"Fans of Marvel or DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel and NOT DC = {marvel_fans.difference(dc_fans)}")
print(f"Fans of EITHER Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 60)
# Combine SETS using SET OPERATORS (Remember VENN diagrams).
print(f"Fans of Marvel or DC = {marvel_fans | dc_fans}")
print(f"Fans of Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel and NOT DC = {marvel_fans - dc_fans}")
print(f"Fans of EITHER Marvel OR DC = {marvel_fans ^ dc_fans}")