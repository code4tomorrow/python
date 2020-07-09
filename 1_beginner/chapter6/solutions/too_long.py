"""
Too Long
Print and remove all elements with length
greater than 4 in a given list of strings.
"""
the_list = ["dragon", "cab", "science", "dove", "lime", "river", "pop"]

for x in the_list:  # iterates through every element in the_list
    if len(x) > 4:  # if element length is greater than 4
        print(x)  # prints element
        the_list.remove(x)  # removes element
