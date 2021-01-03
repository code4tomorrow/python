"""
A magic tuple number for a given element is the
index of the given element’s first occurrence in
the tuple TIMES the number of occurrences of
the given element in the tuple. Given an element
and a tuple, return the magic tuple number. If
the element does not exist in the tuple, return -1.
"""

def magic_tuple_number(given_tup, given_elem):
    elem_count = given_tup.count(given_elem)
    if elem_count != 0:
        return given_tup.index(given_elem) * elem_count
    return -1

print(magic_tuple_number((1,3,"Two",3), 3)) # prints 2
print(magic_tuple_number((1,3,"Bob"),"Cat")) # prints -1
