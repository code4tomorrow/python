# Manipulation
# Modify the following code according to
# the instructions.

nums = []

"""
The following code adds the numbers 0, 10, ... 100
to the list nums, and displays this list.
First, make a copy of nums and store it in the varible more_nums.

Then, clear nums, and add the numbers
2, 7, 12, ... 72 to nums instead.
"""

for i in range(0, 101, 10):
    nums.append(i)
print(nums)

"""
Write the code for the following actions:
Change the 1st element of more_nums to -100.
Change the 2nd element of nums to 0.
Remove the last element from more_nums.
Remove every element divisible by 3 from more_nums.
Insert a 21 after the 20 in more_nums (assume that
you DON'T know the index of 20 ahead of time).
Insert 15 0's in the 3rd-to-last position.
    Sample list after insertions:
    [..., 0, 0, ..., 0, 0, element, element]
Display nums and more_nums.
"""
