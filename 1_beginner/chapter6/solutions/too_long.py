"""
Too Long
Print and remove all elements with length
greater than 4 in a given list of strings.
"""
the_list = ['dragon', 'cab', 'science', 'dove', 'lime', 'river', 'pop']

to_remove = []
for x in the_list:  # iterates through every element in the list
    if len(x) > 4:  # if the element length is greater than 4
        print(x)  # prints the element
        to_remove.append(x)  # appends element to remove list

for y in to_remove:  # iterates through every element meant to be removed
    the_list.remove(y)  # removes element from list
