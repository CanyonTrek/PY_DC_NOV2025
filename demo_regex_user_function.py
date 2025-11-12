#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define, name and call user function
# with optional parameters
"""
    DocString
"""
import re

def search_pattern(pattern=r"^(.)(.).\2\1$", file=r"c:\labs\words"):
    lines = 0
    fh_in = open(file, mode="rt")

    for line in fh_in:
        m = re.search(pattern, line)  # Match 5 char palindromes
        if m:
            lines += 1
            print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
    return lines

search_pattern()
num_lines = search_pattern(r"^.{19}$", r"c:\labs\words")
print(f"Lines matched = {num_lines}")