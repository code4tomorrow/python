# Write a function called remove_duplicates
# The sole parameter of the function should be a list
# The function should look through a list,
# Find all duplicate elements, and remove them
# Sort the resulting list
# YOU MAY NOT USE THE set() function IN PYTHON. Use this problem to practice list iteration!
# Hint: To sort a list, use sorted(list)
# Another hint: Use list.count(element)
# To count the number of times that element appears

# Example: array = [1,1,2,5,4,6,12,3,4,6]
# Result should print [1,2,3,4,5,6,12]

# Write code here

list1 = [1, 1, 2, 5, 4, 6, 12, 3, 4, 6]  # Define your list


def remove_duplicate(array):
    for i in array:
        # Checks if element appears multiple times
        for j in range(i, len(array) - 1):
            #  Counts the number of times an element appears.
            if array.count(array[i]) == 1:
                break  # If it appears once, break out of the loop
            else:
                # If it appears more than once, remove it
                array.remove(array[i])
    return sorted(array)  # Sorts the list


print(remove_duplicate(list1))  # Call the function
