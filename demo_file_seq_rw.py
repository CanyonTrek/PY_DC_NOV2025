#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, and close, for reading, writing
# and appending to a TEXT file
""" 
    DocString
"""
import sys
movies = { 'sian': ['shutter island', 'the grinch', 'zombieland'],
           'courtney': ['matilda', 'this xmas', 'friday'],
           'matt': ['dark knight', 'interstellar', 'the prestige'],
           'tanvi': ['I swear', 'elf', 'harry potter']
}

# Open file handle for WRITING in TEXT mode
fh_out = open(r"c:\labs\projects\LBG_DC_nov2025\movies.txt", mode="wt")

# Iterate through dict keys and write key_values to File
for name in movies.keys():
    print(f"{name}: {movies[name]}", end="\n", file=sys.stdout)
    print(f"{name}: {movies[name]}", end="\n", file=fh_out)
    # fh_out.write(f"{name}: {movies[name]}\n")

fh_out.close() # Flush buffers and cose file handle

print("-" * 60)

# Open file handle for READING in TEXT mode
fh_in = open(r"c:\labs\projects\LBG_DC_nov2025\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str! Careful of HUGE file!
# text = fh_in.read(30) # Read NEXT 30 chars into str!
# text = fh_in.readline() # Read NEXT LINE into str!
# lines = fh_in.readlines() # Read ALL LINES into LIST! Careful of HUGE files
# print(f"First line = {lines[0]}")
# print(f"Last line = {lines[-1]}")

# Alternatively, we could ITERATE through the file handle
# one line at a time using an ITERATOR loop.
for line in fh_in:
    print(line, end="")
fh_in.close()
