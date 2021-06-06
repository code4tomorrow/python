""" O(1) """
# Any assignments
x = 1  # O(1)
x += 1  # O(1)

# If statement structure
# Condition and code inside not always O(1)
if 1 == 1:  # O(1)
    print(1)  # O(1)
else:  # O(1)
    print(2)  # O(1)

# Some list operations
x = [1, 2, 4, 213]
x.append(14)  # O(1)
x[0] = 11  # O(1)


""" O(n) """
# "Most" for loops are O(n)
for number in [123, 4, 21, 312, 41]:  # O(n)
    print(number)  # O(1)


""" O(n^2), O(n^3), etc. """
# "Most" of the time, every extra for loop
# increases running time by a factor of n

example_list = [12, 3, 214, 5, 12]
for num1 in example_list:  # O(n)
    for num2 in example_list:  # O(n)
        print(num1, num2)  # O(n)
