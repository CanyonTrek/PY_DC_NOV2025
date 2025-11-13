#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo 
""" 
    Test Cases for Basic module for testing, add, mul and div functions
"""
import basic

def test_add():
    assert basic.add(4, 3, 2, 1) == 10.0, "Should be 10.0"
    assert basic.add(10, 20) == 30.0, "Should be 30.0"
    return None

def test_mul():
    assert basic.mul(4, 3) == 12.0, "Should be 12.0"
    return None

def test_div():
    assert basic.div(4, 3) == 1.334, "Should be 1.334"
    return None

def main():
    print("Starting Tests..")
    test_add()
    test_mul()
    test_div()
    print("All TESTS Successful")
    return None

if __name__ == "__main__":
    main()