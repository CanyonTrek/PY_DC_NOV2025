#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define, name and call a VARIADIC function
"""
    This program has several Search Functions for matching text data
    in one or more files using Regular Expressions
"""
import re

# Variadic Function which allows variable num of parameters
# captured in a TUPLE called files
def search_pattern(pattern=r"^(.)(.).\2\1$", *files):
    """ Search for Regex Pattern and return num lines matched """
    lines = 0
    for file in files:
        fh_in = open(file, mode="rt")

        for line in fh_in:
            m = re.search(pattern, line)  # Match 5 char palindromes
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
    return lines


num_lines = search_pattern(r"^.{19}$", r"c:\labs\words", r"c:\labs\words2", r"c:\labs\words3")
print(f"Lines matched = {num_lines}")
