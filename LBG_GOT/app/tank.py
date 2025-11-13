#! /usr/bin/env python3
# Author: DCameron
# Description: This module describes a Class of Tank
# for a Tank Game
""" 
    Tank Class
"""
from app import vehicle

class Tank(vehicle.Vehicle):
    # Class has 2 components - Attribute/Data + Behaviour/Methods
    def __init__(self, country, model):
        vehicle.Vehicle.__init__(self, country, model)
        self._direction = 0
        self._location = {"x": 0, "y": 0, "z": 0}
        self._shells = 20
        self._health = 100
        # No Explicit return as its called implicitly

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage

    # Some SPECIAL methods..
    def __add__(self, other):
        return self._health + other._health

    # Example of a GETTER and a SETTER
    def get_health(self):
        return self._health

    def set_health(self, newhealth):
        self._health = newhealth
        return None

    tank_health = property(get_health, set_health)