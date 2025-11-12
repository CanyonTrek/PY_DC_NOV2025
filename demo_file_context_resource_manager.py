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

with open(r"c:\labs\projects\LBG_DC_nov2025\movies.txt", mode="wt") as fh_out:
    for name in movies.keys():
        print(f"{name}: {movies[name]}", end="\n", file=sys.stdout)
        print(f"{name}: {movies[name]}", end="\n", file=fh_out)
    # End of BLOCK, file handle closed

print("-" * 60)

# Open file handle for READING in TEXT mode
with open(r"c:\labs\projects\LBG_DC_nov2025\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")
    # End of block, file handle CLOSED