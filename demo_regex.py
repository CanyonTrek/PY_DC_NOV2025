#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO match lines of Text using
# string testing and Pattern Matching using the re Module.
""" 
    DocString
"""
import re

# Open File handle for READING in TEXT mode
fh_in = open(r"c:\labs\words", mode="rt")

# ITERATE through the file handle one line at a time..
for line in fh_in:
    # Example of str Testing
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    # m = re.search(r"banana", line) # Match lines with 'banana'
    # m = re.search(r"^the", line) # Match line starting with 'the'
    # m = re.search(r"ing$", line) # Match line ending with 'ing'
    # m = re.search(r"^...................$", line) # Match lines of exactly 19 chars
    # m = re.search(r"^.{19}$", line) # Match lines of exactly 19 chars
    # m = re.search(r"^.ing$", line) # Match lines starting with any char followed by "ing"
    # m = re.search(r"^[adr]ing$", line)  # Match lines starting with any [adr] followed by "ing"
    # m = re.search(r"^[A-Z]", line)  # Match lines starting with a CAPITAL
    # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # Match lines with 3 consecutive vowels.
    # m = re.search(r"[aeiou]{5,}", line)  # Match lines with at least 5 consecutive vowels.
    # m = re.search(r"\.", line)  # Match lines with a DOT! Needs to be a RAW string!
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines start/end with a CAPITAL
    # m = re.search(r"^[A-Z].{4}[A-Z]$", line)  # Match lines of 6 chars start/end with a CAPITAL
    m = re.search(r"^(.)(.).\2\1$", line)  # Match 5 char palindromes
    # m = re.search(r"^([A-Z]).*\1$", line)  # Match lines start/end with SAME CAPITAL
    # m = re.match(r"([A-Z]).*\1$", line)  # match() AUTOMATICALLY search START OF LINE!
    # m = re.fullmatch(r"^([A-Z]).*\1\n$", line)  # fullmatch() must match ENTIRE line incl HIDDEN chars
    if m:
        print(m)
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()},"
              f" Grouping = {m.groups()}, Group 1 = {m.group(1)}")
