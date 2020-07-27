# Write a function called remove_duplicates
# The sole parameter of the function should be a list
# The function should look through a list,
# Find all duplicate elements, and remove them
# Sort the resulting list
# YOU MAY NOT USE THE set() function IN PYTHON.
# Hint: To sort a list, use sorted(list)
# Another hint: Use dict.fromkeys(list)
# To take the elements from a list,
# and convert them to keys in a dictionary

# Example: array = [1,1,2,5,4,6,12,3,4,6]
# Result should print [1,2,3,4,5,6,12]

# Write code here

list1 = [1, 1, 2, 5, 4, 6, 12, 3, 4, 6]  # Define your list


# Define your Function
def remove_duplicates(array):
    my_list = list(dict.fromkeys(array))
    # Converts the list into a dictionary.
    # Fromkeys(array) turns each item into a key
    # There cannot be multiple keys,
    # So all the duplicate keys are removed
    # Convert the keys back into a list
    return sorted(my_list)
    # Returns the sorted list of keys that are not duplicate.


print(remove_duplicates(list1))  # Call the function
