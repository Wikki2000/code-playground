#!/usr/bin/env python3
"""Use the addition function from modules/1-math_operations.py"""
add_sibling_to_path = __import__("1-path_helper").add_sibling_to_path
# This is use to add modules directory to python path
# This is done to to import modules from siblings directory
add_sibling_to_path("modules")

from math_operations import addition

result = addition(5, 3)
print("The sum is:", result

