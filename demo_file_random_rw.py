#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, and close, for reading, writing
# and appending to a TEXT file
"""
    DocString
"""

# Open file handle for READING in TEXT mode
with open(r"c:\labs\projects\LBG_DC_nov2025\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, 0) # Seek forwards 90 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(135, 0) # Seek forwards 135 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

# Open file handle for READING in BINARY mode
with open(r"c:\labs\projects\LBG_DC_nov2025\movies.txt", mode="rb") as fh_in:
    fh_in.seek(-70, 2) # Seek back 70 bytes from EOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(-80, 1) # Seek back 80 bytes from current position
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")