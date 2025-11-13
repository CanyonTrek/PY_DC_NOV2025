#! /usr/bin/env python3
# Author: DCameron
# Description: This script is a Calculator App
""" 
    Calculator App with Basic and Advanced functions
"""
import sys
from app import basic
from app import adv

def main():
    while True:
        menu = """
            Menu Options
            ------------
            1.Basic Calc Examples
            2.Adv Calc Examples
            q=quit
        """
        print(menu)
        option = input("Enter option (1-2, q=quit): ")
        if option == "1":
            print(f"20 + 19 + 18 = {basic.add(20, 19, 18)}")
            print(f"20 * 19 * 18 = {basic.mul(20, 19, 18)}")
            print(f"20 / 19 = {basic.div(20, 19)}")
        elif option == "2":
            print(f"20**19 = {adv.power(20, 19)}")
            print(f"20 % 19 = {adv.mod(20, 19)}")
            print(f"\N{square root}20 = {adv.sqrt(20)}")
        elif option == "q":
            break
        else:
            print("Invalid option")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as a module
    main()
    sys.exit(0)