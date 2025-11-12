#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO generate 6
# Random lottery numbers
""" 
    DocString
"""
import random

# lotto = [] # Create Empty list

# while len(lotto) < 6:
#    num = random.randint(1, 50)
#    if num not in lotto:
#       lotto.append(num)
#    else:
#        print("Duplicate number =", num)

lotto = set()

while len(lotto) < 6:
    num = random.randint(1, 50)
    lotto.add(num)


print("Lottery numbers =", sorted(lotto, key=int, reverse=True))
