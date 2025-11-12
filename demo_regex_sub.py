#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo 
""" 
    DocString
"""
import re

# Sample line from /etc/passwd on Linux for root user account
line = r"root:x:0:0:The Super User:/root:/bin/ksh"

line = re.sub(r"[sS]uper [uU]ser", r"Administrator", line) # REturns MODIFIED str
(line, num) = re.subn(r"ksh$", r"bash", line) # Returns TUPLE (mod str, num changes)

print(f"Modified line = {line} with {num} changes")