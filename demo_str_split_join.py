#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO split and join() strings using
# the .split() and .join() methods
""" 
    DocString
"""

# Sample line from /etc/passwd on Linux FS for a user called root.
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# And I want to MODIFY the str! BUT strings are IMMUTABLE!
fields = line.split(":") # Returns a LIST! LISTS are mutable!
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields) # Returne a NEW str object

print("Modified line =", line)