#! /usr/bin/env python3
# Author: DCameron
# Description: This is highly realistic Tank Game
""" 
    GOT - Game of Tanks
"""
import sys
from app import tank

def main():
    # Instantiate/Create 3 new Tank Objects
    jen_tank = tank.Tank("german", "tiger")
    matt_tank = tank.Tank("american", "sherman")
    dave_tank = tank.Tank("british", "churchill")

    # And game begins..
    jen_tank.accel(51)
    matt_tank.accel(32)

    dave_tank.rotate_left(289)
    dave_tank.accel(29)
    dave_tank.shoot()

    # And success..
    jen_tank.take_damage(58)
    matt_tank.take_damage(32)

    # And now for some visuals..
    print(f"Health of Jen's Tank is {jen_tank._health}") # POOR CODE

    print(f"Combined health of Jen's and Matt's health is {jen_tank + matt_tank}")

    # Jen has received a Health Boost
    # jen_tank._health = 100 # POOR CODE
    # print(f"New health of Jen's Tank is {jen_tank._health}") # POOR CODE
    jen_tank.set_health(101) # Setter = GOOD!
    print(f"New health of Jen's Tank is {jen_tank.get_health()}")  # Getter = GOOD

    jen_tank.tank_health = 102
    print(f"New health of Jen's Tank is {jen_tank.tank_health}")  # Getter = GOOD
    return None

# Namespace Trick
if __name__ == "__main__":
    main()
    sys.exit(0)