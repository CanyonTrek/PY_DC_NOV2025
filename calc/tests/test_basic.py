#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo 
""" 
    Test Cases for Basic module for testing, add, mul and div functions
"""
from calc.app import basic
import unittest

class TestBasic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(basic.add(4, 3, 2, 1), 10.0, "Should be 10.0")
        self.assertEqual(basic.add(10, 20), 30.0, "Should be 30.0")
        return None

    def test_mul(self):
        self.assertEqual(basic.mul(4, 3), 12.0, "Should be 12.0")
        return None

    def test_div(self):
        self.assertEqual(basic.div(4, 3), 1.333, "Should be 1.333")
        return None

if __name__ == "__main__":
    unittest.main()