#! /usr/bin/env python3
# Author: DCameron
# Description: This script will simulate a high street bank PIN
# machine using a while condition loop
""" 
    DocString
"""

master_pin = "0123"
pin = None
attempts = 0

while master_pin != pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    # Only execute when too many attempts
    print("Too many attempts")
    print("Your card has been retained. Have a nice day!")

print("Done")