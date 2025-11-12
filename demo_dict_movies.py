#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO create, and grow, and shrink
# dictionaries (Unordered collection with Unique keys). FRom Python 3.6
# dict are NOW in INSERTION ORDER!
""" 
    DocString
"""
import pprint

movies = { 'sian': ['shutter island', 'the grinch', 'zombieland'],
           'courtney': ['matilda', 'this xmas', 'friday'],
           'matt': ['dark knight', 'interstellar', 'the prestige'],
           'tanvi': ['I swear', 'elf', 'harry potter']
}

# Grow a dict
movies['donald'] = ['brave', 'braveheart', 'babe']

# Display dict
pprint.pprint(movies)
print("-" * 60)

films = movies.copy()  # Copies dict
films.clear() # Empties dict

movies.pop('matt') # Remove MAtt's key+value
movies.popitem() # REMOVE LAST INSERTED key+value
pprint.pprint(movies)

print("-" * 60)
# Access dict keys and values
print(f"Sian's favourite movies are {movies['sian']}")
print(f"Sian's favourite movies are {movies.get("sian")}")
print(f"Tanvi's favourite movie is {movies['tanvi'][0]}")

# ITERATE through a dict using an ITERATOR for loop plus...
# .keys() method
for name in movies.keys():
    print(f"{name} likes {movies[name]}")

# .values() method
for films in movies.values():
    print(f"Good films = {films}")

# keys_values using .items() method
for (name, films) in movies.items():
    print(f"{films} recommended by {name}")