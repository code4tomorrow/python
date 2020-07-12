# Lists
my_list = [1, 2, "oh no", 4, 5.62]

# list indexing
print(my_list[1])  # prints 2
print(my_list[3])  # prints 4

# list slicing
print(my_list[1:3])  # prints [2, "oh no"]

# manipulating lists
my_list = []  # empty list

# append() adds elements to the end of the list
my_list.append("live")
my_list.append("long")
my_list.append("and")
my_list.append("prosper")
print(my_list)

# copy() returns a copy of the list
copy_of_my_list = my_list.copy()
print(copy_of_my_list)

# pop() removes the element at the specified index
my_list.pop(2)
print(my_list)

# remove() removes the first item with the specified value
my_list.remove("live")
print(my_list)

# index() returns the index of the first element
# with the specified value
print(my_list.index("prosper"))

# insert() adds an element at the specified position
my_list.insert(0, "live")
print(my_list)

# reverse() reverses the order of the list
my_list.reverse()
print(my_list)

# sort() sorts the list
my_list.sort()
print(my_list)

# clear() removes all elements from the list
my_list.clear()
print(my_list)

# for each item in my_list
for item in my_list:
    # print that item
    print(item)
