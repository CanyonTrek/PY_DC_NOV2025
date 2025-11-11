#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo several different ways of formatting string data.
""" 
    DocString
"""
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# ITERATE through the Dict keys to display planet and distance info
# Using an ITERATOR for loop, plus str concatenation and escape chars - UGLY!
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm")

print("-" * 40)
# Using an ITERATOR for loop, plus str justification methods and concatenation - OK!
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12) + " Gm")

print("-" * 40)
# Using an ITERATOR for loop, plus str .format() method - GOOD!
for planet in planets.keys():
    print("{0:>12s}: {1:>12.3f} Gm".format(planet, planets[planet]))

print("-" * 40)
# Using an ITERATOR for loop, and f-strings (Py3.5) My Favourite!
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:>12.3f} Gm")