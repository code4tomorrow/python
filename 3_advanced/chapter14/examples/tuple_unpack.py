# Switching 2 and 3
list1 = [1, 2, 3, 4, 5]

temp = list1[1]
list1[1] = list1[2]
list1[2] = temp

print(list1)
# prints [1, 3, 2, 4, 5]


list1 = [1, 2, 3, 4, 5]

list1[1], list1[2] = list1[2], list1[1]

print(list1)
# also prints [1, 3, 2, 4, 5]


list1 = [1, 2, 3, 4, 5]

list1[0], list1[1], list1[2] = list1[1], list1[2], list1[0]

print(list1)
# prints [2, 3, 1, 4, 5]
