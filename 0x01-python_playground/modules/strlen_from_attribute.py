#!/usr/bin/python3
"""This module illustrate the use of attributes, to get string lenght"""


class String:
    strlen = 0
    def __init__(self, string):
        """__init__ method
        Initialize and assign the len of the string to public attr (strlen)

        Args:
            str (string): String whoose lenght is to be calculated
        """
        self.string = string
        self.strlen = len(string)
