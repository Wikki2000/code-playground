str = "key1=1 key2=2 key3=4"
my_dict = {}

# Split the string into a list of key-value pairs
str_list = str.split()

# Iterate over each key-value pair
for pair in str_list:
    # Split each pair into key and value using '=' as the separator
    key, value = pair.split("=")
    # Assign the key-value pair to the dictionary
    my_dict[key] = value

print(my_dict)

