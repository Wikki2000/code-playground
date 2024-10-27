#!/usr/bin/python3
"""Read data from csv file to dictionary."""
import csv


file_path = "data.csv"

# Wrap each row as dictionary into an object.
# The first row becomes the key of dictionary.
with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row, "===",  type(row))

print("*********************************")

# Wrap each row as list into an object.
# Unlike DictReader, the first row is still a list.
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row, "===",  type(row))
