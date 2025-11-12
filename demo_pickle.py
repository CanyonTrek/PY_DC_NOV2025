#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo 
""" 
    DocString
"""
#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo HOWTO open, and close, for reading, writing
# and appending to a TEXT file
"""
    DocString
"""
import pickle#
import pprint
import gzip # Others tarfile, shutil, bz2
movies = { 'sian': ['shutter island', 'the grinch', 'zombieland'],
           'courtney': ['matilda', 'this xmas', 'friday'],
           'matt': ['dark knight', 'interstellar', 'the prestige'],
           'tanvi': ['I swear', 'elf', 'harry potter']
}

# Open file handle for WRITING in BINARY mode
# with open(r"c:\labs\projects\LBG_DC_nov2025\movies.p", mode="wb") as fh_out:
with gzip.open(r"c:\labs\projects\LBG_DC_nov2025\movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=1) # Pickle Protocol (0=ASCII, 1-5=Binary)
    pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL)  # Protocol=4

# Open file handle for READING in BINARY mode
# with open(r"c:\labs\projects\LBG_DC_nov2025\movies.p", mode="rb") as fh_in:
with gzip.open(r"c:\labs\projects\LBG_DC_nov2025\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)
