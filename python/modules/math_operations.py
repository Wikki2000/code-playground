#!/usr/bin/env python3
"""
This module contains functions for math operation to be tested.
This is module objective is to illustrate python unnitest.
"""

def addition(x, y):
    """Add two numbers together.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return x + y

def subtraction(x, y):
    """Subtract one number from another.

    Args:
        x (float): The number to subtract from.
        y (float): The number to subtract.

    Returns:
        float: The result of the subtraction.
    """
    return x - y

def division(x, y):
    """Divide one number by another.

    Args:
        x (float): The dividend.
        y (float): The divisor.

    Returns:
        float: The result of the division.
    """
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y
