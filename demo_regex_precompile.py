#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO match lines of Text using
# string testing and Pattern Matching using the re Module.
"""
    DocString
"""
import re
fh_in = open(r"c:\labs\words", mode="rt")

reobj = re.compile(r"^(.)(.).\2\1$") # PRECOPILE pattern ONCE!

for line in fh_in:
    # m = re.search(r"^(.)(.).\2\1$", line)  # Match 5 char palindromes
    m = reobj.search(line)
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}")
