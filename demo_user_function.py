#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO define, name, and call with
# optional parameters and return optional data.
""" 
    DocString
"""

# Example of User function with optional parameter
# passing and default values. Enforce Named parameters using (*,)
# with Annotations (Embedded comment describing preferred type of data)
def say_hello(greeting:str="moi", recipient:str="kaverini"):
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello("hello", "my friends") # Positional parameter passing
say_hello(greeting="bonjour", recipient="mes amis") # Named parameter passing
say_hello(recipient="amici", greeting="ciao") # Named parameter passing (different order)
say_hello("hallo", recipient="mein freunde") # Mixed parameter passing (positional->named)
say_hello("awrite", ['rodanthi', 'sian', 'mike'])
say_hello()