# Given a 2D list, let's call a element "smooth" if index of the
# element in its 1D list plus the element is even. For example,
# given the 2D list [[0,4][2,6]], the 1st element of each of the
# 1D list is considered "smooth" because 0 + 0 is 0 and 0 + 2 is 2
# (both are even numbers). Find the maximum "smooth" element and
# print it. Using the example [[0,4][2,6]] again, the maximum
# "smooth" element is 2 because 2 is bigger than 0.

two_d_list = [[425, 214, 412, 123], [312, 214, 123, 343]]
curr_max = None

for outer_idx in range(len(two_d_list)):
    for inner_idx in range(len(two_d_list[outer_idx])):
        curr_elem = two_d_list[outer_idx][inner_idx]
        to_check = curr_elem + inner_idx
        if to_check % 2 == 0:
            if curr_max is None or curr_elem > curr_max:
                curr_max = curr_elem

print(curr_max)
