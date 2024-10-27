#!/usr/bin/python3
"""Write to a csv file."""
import csv

# Define the path to your CSV file
file_path = 'data.csv'

# New data to be added
new_data = [
    {'Name': 'Alice Johnson', 'Age': 27, 'City': 'Boston'},
    {'Name': 'Bob Williams', 'Age': 31, 'City': 'San Francisco'}
]

# Append new data to the CSV file
with open(file_path, mode='a') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'City'])

    # Write each new row
    for row in new_data:
        writer.writerow(row)

print("************************************")
new_data = [
    ["Alice Johnson", 27, "Boston"],
    ["Bob Williams", 31, "San Francisco"]
]

with open(file_path, mode='a', newline='') as file: # If mode is set to "w" it will over-write
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])  # Write headers
    writer.writerows(new_data)  # Write multiple rows at once

print("New data added successfully!")

